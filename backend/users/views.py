from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDetailView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(User, pk=pk)
            data = UserSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = User.objects.all() 
        data = UserSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password') or None  
            return Response(serializer.data)
        
        return Response({"invalid": "not good data"}, status=400)