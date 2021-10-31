from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Flashcard
from .serializers import FlashcardSerializer
from rest_framework import permissions

# Create your views here.
class FlashList(ListCreateAPIView):

  serializer_class=FlashcardSerializer
  permission_classes=(permissions.IsAuthenticated,)

  def  perform_create(self, serializer):
      serializer.save(name=self.request.user)

  def get_queryset(self):
    return Flashcard.objects.filter(name=self.request.user)    

class FlashDetailView(RetrieveUpdateDestroyAPIView):
  
  serializer_class=FlashcardSerializer
  permission_classes=(permissions.IsAuthenticated,)
  lookup_field="id"


  def get_queryset(self):
    return Flashcard.objects.filter(name=self.request.user)       
