from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles,name="profiles"),
    path("user-profile/<str:pk>/", views.userProfile,name="user-profile"),
    path("login", views.loginPage,name="login"),

]






