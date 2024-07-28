from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
from .models import Article
from .serializers import ArticleSerializer
from . import client

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.public()
    serializer_class = ArticleSerializer

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
       
        if request.user.is_authenticated:
            user = request.user.username
       
        query = request.GET.get('q')
        make_public = str(request.GET.get('make_public')) != '0'
        tags = request.GET.get('tags') or None

        if not query:
            return Response('', status=400)
        
        results = client.perform_search(query, tags=tags, user=user, public=make_public)
        return Response(results)