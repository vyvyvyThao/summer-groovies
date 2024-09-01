from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Class 
from .serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

    @action(detail=True)
    def register(self, request, pk=None):
        print(request, pk)
        # __import__("pdb").set_trace()
        status = request.user.register(self.get_object().title)
        return Response(status)

class ClassGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

class_list_view = ClassGenericViewSet.as_view({'get': 'list'})
class_detail_view = ClassGenericViewSet.as_view({'get': 'retrieve'})



