from django.shortcuts import render
from .serializers import NoteSerializer
from .models import Note
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class NoteList(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
    queryset = Note.objects.all()

class NoteDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
    queryset = Note.objects.all()

    
