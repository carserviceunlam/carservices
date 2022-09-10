from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from vmSystem.apps.admin_website.models.providers import Providers


class ListProvidersView(LoginRequiredMixin, ListView):
    """
    Return all providers created.
    """

    template_name = 'providers/index.html'
    model = Providers
    paginate_by = 30
    context_object_name = 'providers'
