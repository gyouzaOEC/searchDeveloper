from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage,name="login"),
    path("logout/", views.loginPage,name="login"),
    
    path("", views.profiles,name="profiles"),
    path("user-profile/<str:pk>/", views.userProfile,name="user-profile"),

]






