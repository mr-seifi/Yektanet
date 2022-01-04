from rest_framework import serializers
from advertiser_manager.models import Advertiser, Ad, View, Click


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name', 'reg_date']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'img_url', 'link', 'advertiser', 'pub_date', 'approve']


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['id', 'ad', 'viewed_time', 'user_ip']


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['id', 'view', 'clicked_time', 'user_ip']
