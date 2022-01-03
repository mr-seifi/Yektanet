from django.urls import path
from django.views.generic import RedirectView
from . import views
from .views import IndexView, CreateView, CreatedView, ClickRedirectView, StatView

app_name = 'advertiser_manager'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('created/', CreatedView.as_view(), name='created'),
    path('click/<int:view_id>', ClickRedirectView.as_view(), name='click'),
    path('stat/', StatView.as_view(), name='stat')
]
