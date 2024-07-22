from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class TaskList(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()