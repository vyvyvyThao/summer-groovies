from rest_framework import generics
from rest_framework.response import Response
from algoliasearch_django import raw_search

from classes.models import Class
from classes.serializers import ClassSerializer
from . import client
from users.models import User 

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
       
        if request.user.is_authenticated:
            user = request.user.username
       
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != '0'
        tag = request.GET.get('tag') or None

        if not query:
            return Response('', status=400)
        
        results = client.perform_search(query, tags=tag, user=user, public=public)
        # results = raw_search(User, query)
        return Response(results)

class SearchListOldView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q') 
        results = Class.objects.none()

        if q is not None:
            user = None
            
            if self.request.user.is_authenticated:
                user = self.request.user
            
            results = qs.search(q, user=user)
        return results 