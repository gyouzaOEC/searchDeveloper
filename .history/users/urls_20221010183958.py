from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles,name="profiles"),
    path("user-profile/{}", views.userProfile,name="user-profile"),

]






