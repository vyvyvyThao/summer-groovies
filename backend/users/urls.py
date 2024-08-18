from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users-list'),
    # path('search/', views.SearchListView.as_view(), name='user-search'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/update/', views.UserUpdateAPIView.as_view(), name='user-edit'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
]