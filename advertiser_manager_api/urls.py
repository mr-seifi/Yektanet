from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'advertiser_manager_api'
urlpatterns = [
    path('advertisers/', views.AdvertiserList.as_view()),
    path('advertisers/<int:pk>/', views.AdvertiserDetail.as_view()),
    path('ads/', views.AdList.as_view()),
    path('ads/<int:pk>/', views.AdDetail.as_view()),
    path('views/', views.ViewList.as_view()),
    path('views/<int:pk>/', views.ViewDetail.as_view()),
    path('clicks/', views.ClickList.as_view()),
    path('clicks/<int:pk>/', views.ClickDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
