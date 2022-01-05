from django.db import models


class ClickedCount(models.Model):

    date = models.DateTimeField()
    count = models.IntegerField()


class ViewedCount(models.Model):

    date = models.DateTimeField()
    count = models.IntegerField()
