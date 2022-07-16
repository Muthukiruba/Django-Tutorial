from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('projects/', views.projects, name="projects")
]