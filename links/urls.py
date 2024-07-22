from django.urls import path
from .views import LinkList, LinkDetail

urlpatterns = [
    path('list/', LinkList.as_view(), name='list'),
    path('detail/<int:pk>/', LinkDetail.as_view(), name='detail'),
]
