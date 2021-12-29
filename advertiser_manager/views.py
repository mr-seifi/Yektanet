from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advertiser, Ad
from django.views.generic import RedirectView, ListView, TemplateView


class IndexView(ListView):
    model = Advertiser
    template_name = 'advertiser_manager/index.html'
    context_object_name = 'advertisers'
    for adv in Advertiser.objects.all():
        for ad in adv.ad_set.all():
            ad.views += 1
            ad.advertiser.views += 1
            ad.save()
            ad.advertiser.save()


class CreateView(TemplateView):
    template_name = 'advertiser_manager/create.html'


class CreatedView(RedirectView):

    def post(self, request, *args, **kwargs):
        ad = Ad()
        ad.title = request.POST.get('title', False)
        ad.img_url = request.POST.get('img_url', False)
        ad.link = request.POST.get('link', False)
        ad.advertiser = get_object_or_404(Advertiser, pk=int(request.POST.get('adv_id', False)))
        ad.pub_date = request.POST.get('date', False)
        ad.save()
        return HttpResponseRedirect(reverse('advertiser_manager:index', args=()))


class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'click'

    def get(self, request, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        ad.clicks += 1
        ad.advertiser.clicks += 1
        ad.advertiser.save()
        ad.save()
        ClickRedirectView.url = ad.link
        return HttpResponseRedirect('https://google.com')
