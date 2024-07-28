from rest_framework import generics, mixins   #, permissions, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

# from api.authentication import TokenAuthentication
from api.mixins import (StaffEditorPermissionMixin, UserQuerysetMixin)

from .models import Class
from .serializers import ClassSerializer
from api.permissions import IsStaffEditorPermission

from datetime import date

class ClassMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)

        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        start_date = serializer.validated_data.get('start_date') or None

        if start_date is None:
            start_date = date.today()

        serializer.save(start_date=start_date)


class_mixin_view = ClassMixinView.as_view()


# create, read
class ClassListCreateAPIView(
    UserQuerysetMixin,
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def perform_create(self, serializer):
        start_date = serializer.validated_data.get('start_date') or None

        if start_date is None:
            start_date = date.today()

        serializer.save(user=self.request.user, start_date=start_date)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)        
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Class.objects.none()
    #     # print(request.user)
    #     return qs.filter(user=request.user)

class_list_create_view = ClassListCreateAPIView.as_view()


# read
class ClassDetailAPIView(
    StaffEditorPermissionMixin, 
    UserQuerysetMixin, 
    generics.RetrieveAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class_detail_view = ClassDetailAPIView.as_view()


# update
class ClassUpdateAPIView(
    StaffEditorPermissionMixin, 
    UserQuerysetMixin, 
    generics.UpdateAPIView):
    
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.start_date:
            instance.start_date = date.today()

class_update_view = ClassUpdateAPIView.as_view()


# delete
class ClassDestroyAPIView(
    StaffEditorPermissionMixin, 
    UserQuerysetMixin, 
    generics.DestroyAPIView):
    
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class_delete_view = ClassDestroyAPIView.as_view()


@api_view(['GET', 'POST'])
def class_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 

    if method == "GET":
        # detail view
        if pk is not None:
            obj = get_object_or_404(Class, pk=pk)
            data = ClassSerializer(obj, many=False).data
            
            return Response(data)
        
        else:
            qs = Class.objects.all()
            data = ClassSerializer(qs, many=True).data
            
            return Response(data)

    if method == "POST":
        # create an item
        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            start_date = serializer.validated_data.get('start_date') or None

            if start_date is None:
                start_date = date.today()

            serializer.save(start_date=start_date)           ## THIS DOESN'T WORK AT ALL
           
            return Response(serializer.data)
        return Response({"Invalid": "not good data"}, status=400)
    
    if method == "PUT":
        # create an item
        serializer = ClassSerializer(data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response({"Invalid": "not good data"}, status=400)