from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('joblist/', views.joblist, name='joblist')
]