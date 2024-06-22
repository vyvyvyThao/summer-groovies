from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_mixin_view),
    path('<int:pk>/update/', views.class_update_view),
    path('<int:pk>/delete/', views.class_delete_view),
    path('<int:pk>/', views.class_mixin_view)
]