from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

app_name = 'advertiser_manager_api'

router = DefaultRouter()
router.register(r'advertisers', views.AdvertiserViewSet)
router.register(r'ads', views.AdViewSet)
router.register(r'views', views.ViewViewSet)
router.register(r'clicks', views.ClickViewSet)

urlpatterns = [
    path('', include(router.urls))
]
