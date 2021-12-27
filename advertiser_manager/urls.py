from django.urls import path
from . import views

app_name = 'advertiser_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path(r'created/', views.created, name='created'),
]
