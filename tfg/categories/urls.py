from rest_framework import routers

from .viewsets import CategoryViewSet, PointPackViewSet

router = routers.SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('point-packs', PointPackViewSet)

urlpatterns = router.urls
