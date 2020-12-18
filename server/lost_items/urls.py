from rest_framework.routers import DefaultRouter

from lost_items.viewsets import LostItemViewSet

router = DefaultRouter()
router.register('', LostItemViewSet)

urlpatterns = router.urls
