from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    reg_date = models.DateTimeField('date registered')

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
