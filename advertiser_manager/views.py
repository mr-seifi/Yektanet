from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advertiser, Ad
from django.views.generic import RedirectView


def index(request):
    advertiser_list = Advertiser.objects.all()
    for adv in advertiser_list:
        for ad in adv.ad_set.all():
            ad.views += 1
            ad.advertiser.views += 1
            ad.save()
            ad.advertiser.save()
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


# class ClickRedirectView(RedirectView):
#
#     permanent = False
#     query_string = True
#     pattern_name = 'click'
#
#     def get_redirect_url(self, *args, **kwargs):
#         ad = get_object_or_404(Ad, pk=kwargs['pk'])
#         ad.clicks += 1
#         ad.advertiser.clicks += 1
#         ad.advertiser.save()
#         ad.save()
#         ClickRedirectView.url = ad.link
#         return super().get_redirect_url(*args, **kwargs)

def click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.clicks += 1
    ad.advertiser.clicks += 1
    ad.advertiser.save()
    ad.save()
    url = ad.link
    return HttpResponseRedirect(url)
