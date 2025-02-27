from rest_framework.serializers import ModelSerializer

from .models import Player

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        depth = 1