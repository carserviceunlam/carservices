import sys

# Forms
from CarService.apps.admin_website.forms.employee_form import EmployeeForm
from CarService.apps.admin_website.models.cities import Cities
from CarService.apps.admin_website.models.employee import Employee
from CarService.apps.admin_website.views.serializers.employee_serializer import (
    EmployeeSerializer,
)

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, View


class EmployeePage(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    class to handler index view.
    return: index view with the list of employees
    """

    permission_required = "admin_website.view_employee"

    username = None
    template_name = "employees/index.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            EmployeePage.username = self.request.user.username[:4]
            # print(EmployeePage.username)
        print(self.request.user.get_all_permissions())
        employees = Employee.objects.all()
        return render(request, self.template_name, {"employees": employees})

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(request, "No tienes contratado este modulo")
            return redirect(reverse_lazy("index"))
        return super().dispatch(request, *args, **kwargs)


class EmployeeCreate(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    """
    Class to handler Create view.
    return: Create the user, and is succesful return to main employee page
    """

    permission_required = "admin_website.view_employee"

    template_name = "employees/create_employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employees_list")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class EmployeeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class to handler delete user
    return: Delete the user, and is succesful return the main employee page
    """

    permission_required = "admin_website.view_employee"

    model = Employee

    # required by the Class based view
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employees_list")


class EmployeeDetailView(LoginRequiredMixin, View):
    """
    class to handler detail view
    return: the resource uri requested
    """

    template_name = "employees/detail.html"

    def get(self, request, *args, **kwargs):
        form = EmployeeForm
        queryset = Employee.objects.get(cuil=kwargs["cuil"])
        cities = Cities.objects.all()

        return render(
            request=request,
            template_name=self.template_name,
            context={"employees": queryset, "form": form, "cities": cities},
        )

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, context="update", identity_key=kwargs["cuil"])
        if form.is_valid():
            data = form.cleaned_data
            employee_serializer = EmployeeSerializer(data, kwargs["cuil"])
            try:
                employee_serializer.employee_update()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                # Warning lazy except
                # TODO: make a nice try and except
                pass
            return redirect("employees_list")
        else:
            cities = Cities.objects.all()
            return render(
                request=request,
                template_name="employees/detail.html",
                context={"employee": Employee, "form": form, "cities": cities},
            )
