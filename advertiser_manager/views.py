from django.shortcuts import render
from .models import Advertiser, Ad


def index(request):
    advertiser_list = Advertiser.objects.all()
    context = {'advertisers': advertiser_list}
    return render(request, 'advertiser_manager/index.html', context)
