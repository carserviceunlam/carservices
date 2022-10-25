from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, ListView
from django.views.generic.edit import UpdateView
from CarService.apps.admin_website.forms.budget_form import BudgetForm
from CarService.apps.admin_website.models.budgets import Budget


class BudgetList(LoginRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with te list of the budgets
    """

    template_name = "budgets/index.html"
    models = Budget
    paginate_by = 30
    context_object_name = "budgets"

    def get_queryset(self):
        """return all budgets"""
        queryset = Budget.objects.all()
        return queryset


class BudgetDetailView(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ["owner", "state", "detail", "real_cost", "estimated_cost"]
    # remember this is looking for a template with prefix classmodel
    template_name = "budgets/budget_update_form.html"
    success_url = reverse_lazy("budget_list")


class BudgetCreateView(LoginRequiredMixin, FormView):
    """
    class to handler a create view
    return: create the budget. is success return to main budget page
    """

    template_name = "budgets/create.html"
    form_class = BudgetForm
    success_url = reverse_lazy("budget_list")

    def form_valid(self, form):
        """save form data."""
        form.save()
        return super().form_valid(form)


class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    """
    class to delete register
    return a view to accept delete the record.
    """

    model = Budget

    template_name = "budgets/budget_delete_confirm_delete.html"
    success_url = reverse_lazy("budget_list")
