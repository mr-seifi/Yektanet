from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'advertiser_manager_api'
urlpatterns = [
    path('advertisers/',),
    path('ads/',),
    path('views/',),
    path('clicks/',),
]

urlpatterns = format_suffix_patterns(urlpatterns)
