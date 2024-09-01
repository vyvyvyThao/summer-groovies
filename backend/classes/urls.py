from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.class_list_create_view, name='class-list'),
#     path('<int:pk>/update/', views.class_update_view, name='class-edit'),
#     path('<int:pk>/delete/', views.class_delete_view),
#     path('<int:pk>/', views.class_detail_view, name='class-detail')
# ]

from rest_framework.routers import DefaultRouter

from classes.viewsets import ClassViewSet

router = DefaultRouter()
router.register('', ClassViewSet, basename='classes')
urlpatterns = router.urls