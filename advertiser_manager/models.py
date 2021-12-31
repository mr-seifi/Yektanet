from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date registered')

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class View(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    viewed_time = models.DateTimeField('date viewed')
    user_ip = models.CharField(max_length=30)


class Click(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    clicked_time = models.DateTimeField('date clicked')
    user_ip = models.CharField(max_length=30)
