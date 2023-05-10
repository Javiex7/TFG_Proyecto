from rest_framework import routers

from .viewsets import ProfileViewSet

router = routers.SimpleRouter()
router.register('profiles', ProfileViewSet)

urlpatterns = router.urls
