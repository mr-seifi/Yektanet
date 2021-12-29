from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'advertiser_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('created/', views.created, name='created'),
    path('click/<int:ad_id>', views.click, name='click')
]
