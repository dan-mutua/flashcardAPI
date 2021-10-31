from  .views import FlashList,FlashDetailView
from  django.urls import path

urlpatterns = [
  path('',FlashList.as_view(),), 
  path('<int:id>', FlashDetailView.as_view(),)
]