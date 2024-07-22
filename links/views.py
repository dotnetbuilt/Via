from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Link
from .serializers import LinkSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class LinkList(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

class LinkDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = LinkSerializer
    queryset = Link.objects.all()