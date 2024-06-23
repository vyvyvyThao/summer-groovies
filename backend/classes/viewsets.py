from rest_framework import viewsets, mixins

from .models import Class 
from .serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

class ClassGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

class_list_view = ClassGenericViewSet.as_view({'get': 'list'})
class_detail_view = ClassGenericViewSet.as_view({'get': 'retrieve'})



