from django.urls import path

from . import views
from articles.views import SearchListView as ArticleSearchView
from users.views import SearchListView as UserSearchView

urlpatterns = [
    path('', views.SearchListView.as_view(), name='search'),
    path('articles/', ArticleSearchView.as_view(), name='article-search'),
    path('users/', UserSearchView.as_view(), name='user-search')
]
