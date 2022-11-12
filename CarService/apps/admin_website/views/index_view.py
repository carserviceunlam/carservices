from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from CarService.apps.admin_website.forms.budget_form import BudgetForm
from CarService.apps.admin_website.models.budgets import Budget
import MySQLdb


class IndexView(LoginRequiredMixin, ListView):
    """
    class to handler the index view
    return: index view with te list of the budgets
    """

    template_name = "index.html"

    def get_queryset(self):
        IndexView.database = self.request.user.username[:4]
        website = self.request.user.username[5:]
        """conn = MySQLdb.connect(
            host="carservicedb.cvkrx6mlzyev.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="Service2022",
            db="carservicedb",
        )
        cursor1 = conn.cursor()
        cursor1.execute("SELECT id FROM carservicedb.service_customer WHERE ")
        cursor1.close()
        conn.close()"""
        # print(database)
        queryset = Budget.objects.all()
        return queryset