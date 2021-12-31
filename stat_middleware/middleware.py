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
            self.clickInc(request)

    @staticmethod
    def viewInc(request):
        for ad in Ad.objects.all():
            if not ad.approve:
                continue
            v = View()
            v.ad_id = ad
            v.viewed_time = timezone.now()
            v.user_ip = request.META['REMOTE_ADDR']
            v.save()

    @staticmethod
    def clickInc(request):
        c = Click()
        c.ad_id = Ad.objects.get(pk=re.findall(r'\/advertiser\/click\/(\d+)', request.path)[0])
        c.clicked_time = timezone.now()
        c.user_ip = request.META['REMOTE_ADDR']
        c.save()
