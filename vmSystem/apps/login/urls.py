from django.urls import path
from vmSystem.apps.login import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/<str:username>/", views.ProfileView.as_view(), name="profile"),
]
