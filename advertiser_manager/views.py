from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advertiser, Ad


def index(request):
    advertiser_list = Advertiser.objects.all()
    for adv in advertiser_list:
        for ad in adv.ad_set.all():
            ad.views += 1
            ad.save()
    context = {'advertisers': advertiser_list}
    return render(request, 'advertiser_manager/index.html', context)


def create(request):
    return render(request, 'advertiser_manager/create.html', {'ad_id': len(Ad.objects.all())})


def created(request):
    ad = Ad()
    ad.title = request.POST.get('title', False)
    ad.img_url = request.POST.get('img_url', False)
    ad.link = request.POST.get('link', False)
    ad.advertiser = get_object_or_404(Advertiser, pk=int(request.POST.get('adv_id', False)))
    ad.pub_date = request.POST.get('date', False)
    ad.save()
    return HttpResponseRedirect(reverse('advertiser_manager:index', args=()))
