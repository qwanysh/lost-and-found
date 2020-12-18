from rest_framework import serializers

from lost_items.models import LostItem


class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'
