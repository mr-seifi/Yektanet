from __future__ import absolute_import, unicode_literals
import datetime
from celery import shared_task
from advertiser_manager.models import Click, View
from django.utils import timezone
from .models import ClickedCount, ViewedCount
from django.db.models import Sum


@shared_task
def clickHourly():
    now = timezone.now() - datetime.timedelta(hours=1)
    instance = ClickedCount()
    instance.date, instance.count = now, Click.objects.filter(clicked_time__hour=now.hour).count()
    instance.save()


@shared_task
def viewHourly():
    now = timezone.now() - datetime.timedelta(hours=1)
    instance = ViewedCount()
    instance.date, instance.count = now, View.objects.filter(viewed_time__hour=now.hour).count()
    instance.save()


@shared_task
def clickDaily():
    now = timezone.now() - datetime.timedelta(days=1)
    return ClickedCount.objects.filter(date__year=now.year,
                                       date__month=now.month,
                                       date__day=now.day,
                                       date__hour=now.hour).aggregate(Sum('count'))


@shared_task
def viewDaily():
    now = timezone.now() - datetime.timedelta(days=1)
    return ViewedCount.objects.filter(date__year=now.year,
                                      date__month=now.month,
                                      date__day=now.day,
                                      date__hour=now.hour).aggregate(Sum('count'))
