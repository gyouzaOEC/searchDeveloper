from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes,),
    path("projects/", views.getProjects,),
    path("project/<str:pk>/", views.getProject,),
]