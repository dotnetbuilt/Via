from django.urls import path
from .views import NoteList, NoteDetail

urlpatterns = [
    path('list/', NoteList.as_view(), name='list'),
    path('detail/<int:pk>', NoteDetail.as_view(), name='detail'),
]
