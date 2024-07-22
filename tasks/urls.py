from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('list/', TaskList.as_view(), name='list'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
]
