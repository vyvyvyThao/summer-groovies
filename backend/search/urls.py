from django.urls import path

from . import views
from articles.views import SearchListView as ArticleSearchView

urlpatterns = [
    path('', views.SearchListView.as_view(), name='search'),
    path('articles/', ArticleSearchView.as_view(), name='article-search')
]
