from django.urls import include, path
from . import views

urlpatterns = [
   path("", include("django.contrib.auth.urls")),
   path("sign-up", views.view_sign_up),
]