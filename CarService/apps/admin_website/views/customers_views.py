from webbrowser import get
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, View, ListView
from django.views.generic.edit import UpdateView
from CarService.apps.admin_website.forms.customer_form import CustomerFormSet
from CarService.apps.admin_website.models.customer import Customer
from CarService.apps.admin_website.models.cities import Cities
from CarService.apps.admin_website.forms.business_form import BusinessForm
from CarService.apps.admin_website.models.bank_accounts import BankAccounts


class CustomerView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with the list of employees
    """

    permission_required = "admin_website.view_customer"

    # username = None
    template_name = "customers/index.html"
    model = Customer
    paginate_by = 30
    context_object_name = "customers"

    def get(self, request, *args, **kwargs):
        # if self.request.user.is_authenticated:
        #    CustomerView.username = self.request.user.username
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Return all customers queryset"""
        # databse_name = CustomerView.username
        # queryset = Customer.objects.using(databse_name)
        queryset = Customer.objects.all()
        return queryset


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    """
    Class to handle crate view
    return: create the user. if success, return to main customer view
    """

    permission_required = "admin_website.view_customer"

    template_name = "customers/create_customer.html"
    form_class = CustomerFormSet
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        """Save form data."""

        form.save()
        return super().form_valid(form)


class CustomerCreateBusiness(LoginRequiredMixin, FormView):
    """
    Class to handle create view for business customer
    return: create the business, If success, return to main customer view
    """

    template_name = "customers/create_business.html"
    form_class = BusinessForm
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        """save form data"""
        form.save()
        return super().form_valid(form)


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class to handle delete view
    return: if success return to main view
    """

    permission_required = "admin_website.view_customer"

    model = Customer

    # required by the clased delete view
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer_list")


class CustomerDetailView(LoginRequiredMixin, View):
    """
    class to handler detail view
    return: the resource uri requested
    """

    template_name = "customers/detail.html"

    def get(self, request, *args, **kwargs):
        form = CustomerFormSet
        queryset = Customer.objects.get(id=kwargs["id"])
        cities = Cities.objects.all()

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "customer": queryset,
                "form": form,
                "cities": cities,
            },
        )

    def post(self, request, *args, **kwargs):
        data = self._serialize_data(request)
        form = CustomerFormSet(request.POST)
        if form.is_valid():
            form.update(data, _id=kwargs["id"])
            return redirect("customer_list")
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={"customer": Customer, "form": form},
            )

    def _serialize_data(self, request):
        data = {
            "cuit": request.POST["cuit"],
            "business_name": request.POST["business_name"],
            "dni": request.POST["dni"],
            "name": request.POST["name"],
            "last_name": request.POST["last_name"],
            "birth_day": request.POST["birth_day"],
            "phone": request.POST["phone"],
            "mobile": request.POST["mobile"],
            "email": request.POST["email"],
            "city": request.POST["city"],
            "address": request.POST["address"],
            "address_number": request.POST["address_number"],
        }
        return data


class CustomerUpdateBusinessView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ["cuit", "business_name"]
    template_name = "customers/update_business.html"
    success_url = reverse_lazy("customer_list")
