import sys
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, FormView, ListView, View
from vmSystem.apps.admin_website.models.repair import Repair
from django.urls import reverse_lazy
from vmSystem.apps.admin_website.forms.repair_form import RepairForm, RepairUpdateForm
from vmSystem.apps.admin_website.models.budgets import Budget
from django.shortcuts import render, redirect
from vmSystem.apps.admin_website.views.serializers.repair_serializer import (
    RepairSerializer
)


class RepairList(LoginRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with the list of repairs
    """
    template_name = "repairs/index.html"
    models = Repair
    paginate_by = 30
    context_object_name = "repairs"

    def get_queryset(self):
        """return all repairs."""
        queryset = Repair.objects.all()
        return queryset


class RepairUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = RepairUpdateForm
        repair_item = Repair.objects.get(id=kwargs['id'])
        budgets = Budget.objects.all()

        return render(
            request=request,
            template_name="repairs/repair_update_form.html",
            context={
                "repair_item": repair_item,
                "form": form,
                "budgets": budgets,

            }
        )

    def post(self, request, *args, **kwargs):
        form = RepairUpdateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            repair_serializer = RepairSerializer(data, kwargs['id'])
            try:
                repair_serializer.update_repair()
            except:
                print("Unexpected error:", sys.exc_info()[0])
                # Warning lazy except
                # TODO: make a nice try and except
                pass
            return redirect("repair_list")
        else:
            repair_item = Repair.objects.get(id=kwargs['id'])
            budgets = Budget.objects.all()
            return render(
                request=request,
                template_name="repairs/repair_update_form.html",
                context={
                    "repair_item": repair_item,
                    "form": form,
                    "budgets": budgets
                },
            )


class RepairDetailView():
    pass


class RepairCreateView(LoginRequiredMixin, FormView):
    """
    class to handler a create view
    return: create the repair object. is success return to main repair page.
    """
    template_name = "repairs/create.html"
    form_class = RepairForm
    success_url = reverse_lazy("repair_list")

    def form_valid(self, form):
        """save form data."""
        form.save()
        return super().form_valid(form)


class RepairDeleteView(LoginRequiredMixin, DeleteView):
    """
    class to delete register
    return: a view to accept delete record.
    """

    model = Repair

    template_name = "repairs/repairs_delete_confirm_delete.html"
    success_url = reverse_lazy("repair_list")
