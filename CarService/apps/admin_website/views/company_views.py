# Django
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)

# Forms
from CarService.apps.admin_website.forms.companies_form import (
    CompanyForm,
    CreateCompanyForm,
)

# Models
from CarService.apps.admin_website.models.bank_accounts import BankAccounts
from CarService.apps.admin_website.models.cities import Cities
from CarService.apps.admin_website.models.companies import Companies


class ListCompaniesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Return all providers created.
    """

    permission_required = "admin_website.view_companies"

    template_name = "companies/index.html"
    model = Companies
    paginate_by = 30
    context_object_name = "companies"

    def get_queryset(self):
        """Return only companies without providers."""
        queryset = Companies.objects.filter(company_type="Aseguradora").order_by("id")
        return queryset

    def get_context_data(self, **kwargs):
        """Add another object to context."""
        context = super().get_context_data(**kwargs)
        active_companies = Companies.objects.filter(state="Activa")
        total_companies = Companies.objects.filter(company_type="Aseguradora")
        try:
            active_percent = int((len(active_companies) * 100) / len(total_companies))
        except:
            active_percent = 0
        context["active_percent"] = active_percent
        return context


class EditCompanyView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Edit company view."""

    permission_required = "admin_website.view_companies"

    def get(self, request, *args, **kwargs):
        form = CompanyForm()
        company = Companies.objects.get(id=kwargs["id"])
        cities = Cities.objects.all()

        return render(
            request=request,
            template_name="companies/edit.html",
            context={"companies": company, "form": form, "cities": cities},
        )

    def post(self, request, *args, **kwargs):
        company = Companies.objects.get(id=kwargs["id"])
        form = CompanyForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # Bank Account
            bank_acc = BankAccounts.objects.get(cbu=company.bank_account.cbu)
            bank_acc.cbu = data["bank_account_cbu"]
            bank_acc.bank = data["bank_account_name"]
            bank_acc.save()

            # City
            new_city = Cities.objects.get(pk=data["city_name"])

            # Entire Company object
            company.city = new_city
            company.cuit = data["cuit"]
            company.business_name = data["business_name"]
            company.contact_person = data["contact_person"]
            company.phone = data["phone"]
            company.mobile = data["mobile"]
            company.address = data["address"]
            company.address_number = data["address_number"]
            company.email = data["email"]
            company.website = data["website"]
            company.details = data["details"]
            company.state = data["state"]
            company.save()

            return redirect("companies_list")
        else:
            return render(
                request=request,
                template_name="companies/edit.html",
                context={"companies": company, "form": form},
            )


class CreateCompanyView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class to handler Create view.
    """

    permission_required = "admin_website.view_companies"

    def get(self, request, *args, **kwargs):
        form = CreateCompanyForm()
        return render(
            request=request,
            template_name="companies/create.html",
            context={"form": form},
        )

    def post(self, request, *args, **kwargs):
        form = CreateCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("companies_list")
        else:
            return render(
                request=request,
                template_name="companies/edit.html",
                context={"form": form},
            )


class CompanyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    class to delete register
    return a view to accept delete the record
    """

    permission_required = "admin_website.view_companies"

    model = Companies

    template_name = "companies/companies_delete_confirm_delete.html"
    success_url = reverse_lazy("companies_list")
