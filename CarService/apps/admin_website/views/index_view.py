from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from CarService.apps.admin_website.forms.budget_form import BudgetForm
from CarService.apps.admin_website.models.budgets import Budget


class IndexView(LoginRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with te list of the budgets
    """

    template_name = "index.html"

    def get_queryset(self):
        queryset = Budget.objects.all()
        return queryset