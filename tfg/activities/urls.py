from rest_framework import routers

from .viewsets import UserQuizViewSet

router = routers.SimpleRouter()
router.register('quizzes', UserQuizViewSet)

urlpatterns = router.urls
