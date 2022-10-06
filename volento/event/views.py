from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import *
from .serializers import *

# Create your views here.
class EventCategoryList(generics.ListCreateAPIView):
    queryset=EventCategory.objects.all()
    serializer_class=EventCategorySerializer

class EventSponserList(generics.ListCreateAPIView):
    queryset=EventSponser.objects.all()
    serializer_class=EventSponserSerializer

class EventList(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=EventSerializer

class EventImageList(generics.ListCreateAPIView):
    queryset=EventImage.objects.all()
    serializer_class=EventImageSerializer

class EventAgendaList(generics.ListCreateAPIView):
    queryset=EventAgenda.objects.all()
    serializer_class=EventAgendaSerializer

class EventMemberList(generics.ListCreateAPIView):
    queryset=EventMember.objects.all()
    serializer_class=EventMemberSerializer

class EventUserWishListList(generics.ListCreateAPIView):
    queryset=EventUserWishList.objects.all()
    serializer_class=EventUserWishListSerializer

class UserCoinList(generics.ListCreateAPIView):
    queryset=UserCoin.objects.all()
    serializer_class=UserCoinSerializer




