from rest_framework.routers import DefaultRouter

from social_media.views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = router.urls
