from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list_create_view),
    path('<int:pk>/update/', views.class_update_view),
    path('<int:pk>/delete/', views.class_delete_view),
    path('<int:pk>/', views.class_detail_view)
]