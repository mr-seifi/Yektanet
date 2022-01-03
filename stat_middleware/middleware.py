import re
from advertiser_manager.models import Ad, View, Click
from django.utils import timezone


class StatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == '/advertiser/':
            self.viewInc(request)
        if '/advertiser/click' in request.path:
            self.clickInc(request, view_args, view_kwargs)

    @staticmethod
    def viewInc(request):
        for ad in Ad.objects.filter(approve=True):
            v = View()
            v.ad = ad
            v.viewed_time = timezone.now()
            v.user_ip = request.META['REMOTE_ADDR']
            v.save()

    @staticmethod
    def clickInc(request, args, kwargs):
        c = Click()
        c.view = View.objects.get(pk=kwargs['view_id'])
        c.clicked_time = timezone.now()
        c.user_ip = request.META['REMOTE_ADDR']
        c.save()
