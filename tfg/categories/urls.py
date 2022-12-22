from rest_framework import routers

from .viewsets import CategoryViewSet

router = routers.SimpleRouter()
router.register('categories', CategoryViewSet)

urlpatterns = router.urls
