from django.urls import include, path

from authentication import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.auth_logout, name="logout"),
]
