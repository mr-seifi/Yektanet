from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Advertiser, Ad, View, Click
from django.views.generic import RedirectView, ListView, TemplateView
from django.db.models.functions import TruncHour
from django.db.models import Count, Avg, F


class IndexView(ListView):
    model = Advertiser
    template_name = 'advertiser_manager/index.html'
    context_object_name = 'advertisers'

    def get(self, request, *args, **kwargs):
        return super(IndexView, self).get(request, *args, **kwargs)


class CreateView(TemplateView):
    template_name = 'advertiser_manager/create.html'


class CreatedView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'advertiser_manager:index'

    def post(self, request, *args, **kwargs):
        ad = Ad()
        ad.title = request.POST.get('title', 'defaultTitle')
        ad.img_url = request.POST.get('img_url', 'defaultImgUrl')
        ad.link = request.POST.get('link', 'https://google.com')
        ad.advertiser = get_object_or_404(Advertiser, pk=int(request.POST.get('adv_id')))
        ad.pub_date = request.POST.get('date', timezone.now())
        ad.save()
        return super(CreatedView, self).post(request, *args, **kwargs)


class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'advertiser_manager:click'

    def get_redirect_url(self, *args, **kwargs):
        """
        Return the URL redirect to. Keyword arguments from the URL pattern
        match generating the redirect request are provided as kwargs to this
        method.
        """
        return get_object_or_404(View, pk=kwargs['view_id']).ad.link

    def get(self, request, *args, **kwargs):
        return super(ClickRedirectView, self).get(request, *args, **kwargs)


class StatView(TemplateView):
    template_name = 'advertiser_manager/stat.html'

    def get_context_data(self, **kwargs):
        data = []
        for ad in Ad.objects.order_by('-pub_date'):
            clicked = 0
            for view in ad.view_set.all():
                clicked += view.click_set.count()
            data.append((ad, clicked / ad.view_set.count()))
        context = {
            'clicked_sum': Click.objects.annotate(hour=TruncHour('clicked_time')).values('hour').annotate(
                c=Count('id')).values('hour', 'c'),
            'viewed_sum': View.objects.annotate(hour=TruncHour('viewed_time')).values('hour').annotate(
                c=Count('id')).values('hour', 'c'),
            'rate_data': data,
            'avg_diff_click_view': Click.objects.annotate(diff=F('clicked_time') - F('view__viewed_time')).aggregate(Avg('diff'))['diff__avg']
                }
        kwargs.update(context)
        return super(StatView, self).get_context_data(**kwargs)
