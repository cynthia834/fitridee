from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('bicycles/', views.bicycle_list, name='bicycle_list'),
    path('upload/', views.upload_bicycle, name='upload_bicycle'),
    path('', views.home, name='home'),
]
