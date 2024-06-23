from rest_framework.routers import DefaultRouter

from classes.viewsets import ClassViewSet

router = DefaultRouter()
router.register('classes', ClassViewSet, basename='classes')
urlpatterns = router.urls