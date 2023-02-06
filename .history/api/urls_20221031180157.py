from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes,name=""),
    path("", views.getRoutes,name=""),
]