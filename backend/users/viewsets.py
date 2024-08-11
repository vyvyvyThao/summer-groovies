from rest_framework import viewsets, mixins

from .models import User 
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class_list_view = UserGenericViewSet.as_view({'get': 'list'})
class_detail_view = UserGenericViewSet.as_view({'get': 'retrieve'})



