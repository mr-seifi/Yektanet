from advertiser_manager.models import Advertiser, Ad, View, Click
from advertiser_manager_api.serializers import AdvertiserSerializer, AdSerializer, ViewSerializer, ClickSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import viewsets


class AdvertiserViewSet(viewsets.ModelViewSet):

    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    permission_classes = [IsAuthenticated]


class AdViewSet(viewsets.ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permissions = [IsAuthenticatedOrReadOnly]


class ViewViewSet(viewsets.ModelViewSet):

    queryset = View.objects.all()
    serializer_class = ViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClickViewSet(viewsets.ModelViewSet):

    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
