from .models import Flashcard
from rest_framework.serializers import ModelSerializer


class FlashcardSerializer(ModelSerializer):

  class Meta:
    model=Flashcard

    fields=['name','subject','body','is_complete']