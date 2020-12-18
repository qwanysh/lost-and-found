from rest_framework.viewsets import ModelViewSet

from lost_items.models import LostItem
from lost_items.serializers import LostItemSerializer


class LostItemViewSet(ModelViewSet):
    serializer_class = LostItemSerializer
    queryset = LostItem.objects.all()
