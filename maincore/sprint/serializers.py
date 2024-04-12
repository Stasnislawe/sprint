from rest_framework import serializers
from .models import User, Coords, DifficultyLevel, AddMount, Images


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'name',
            'surname',
            'email',
            'phone',
        )
