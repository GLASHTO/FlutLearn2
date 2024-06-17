from .models import MyUser
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    ListAPIView
)
from .serializers import (
    UserCreateSerializer
)

class UserCreateView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserCreateSerializer
