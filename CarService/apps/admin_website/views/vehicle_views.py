from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, View, ListView
from CarService.apps.admin_website.forms.vehicle_form import VehicleForm
from CarService.apps.admin_website.models.companies import Companies
from CarService.apps.admin_website.models.customer import Customer
from CarService.apps.admin_website.models.vehicle_owner import VehicleOwner
from CarService.apps.admin_website.models.vehicles import Vehicles


class VehicleView(LoginRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with the list of vehicles
    """

    template_name = "vehicles/index.html"
    model = Vehicles
    paginate_by = 30
    context_object_name = "vehicles"

    def get_queryset(self):
        """return all vehicles queryset"""
        queryset = Vehicles.objects.all()
        return queryset


class VehicleDetailView(LoginRequiredMixin, FormView):
    """
    class to handler the detail view of the vehicle
    return: index view with te list of vehicles
    """
    template_name = "vehicles/detail.html"

    def get(self, request, *args, **kwargs):
        form = VehicleForm
        queryset = Vehicles.objects.get(id=kwargs["id"])
        companies = Companies.objects.all()
        customers = Customer.objects.all()
        vehicles_owners = VehicleOwner.objects.get(vehicle=queryset.id)

        return render(
            request=request,
            template_name=self.template_name,
            context={"vehicles": queryset,
                     "companies": companies,
                     "customers": customers,
                     "vehicles_owner": vehicles_owners,
                     "form": form}
        )

    def post(self, request, *args, **kwargs):
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.update(_id=kwargs["id"])
            return redirect("vehicles_list")
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={"vehicles": Vehicles, "form": form},
            )


class VehicleCreateView(LoginRequiredMixin, FormView):
    """
    class to handler a create view of vehicle
    return: create the vehicle. and is success return to main vehicle page
    """

    template_name = "vehicles/create_vehicle.html"
    form_class = VehicleForm
    success_url = reverse_lazy("vehicles_list")

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class VehicleDelete(LoginRequiredMixin, DeleteView):
    """
    class to delete register
    return a view to accept delete the record
    """

    model = Vehicles

    template_name = "vehicles/vehicle_delete_confirm_delete.html"
    success_url = reverse_lazy("vehicles_list")
