from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_post ),
    path("", views.all_post_list),
]
