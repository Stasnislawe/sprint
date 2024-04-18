from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'name',
            'surname',
            'otc',
            'email',
            'phone',
        ]

class CoordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height',
        ]


class DifficultyLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DifficultyLevel
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring',
        ]


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Images
        fields = ['image',
                  'title', ]

class AddMountSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coord = CoordsSerializer()
    level = DifficultyLevelSerializer()
    images = ImageSerializer(many=True)
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AddMount
        fields = [
            'id',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coord',
            'status',
            'level',
            'images',
        ]

        read_only_fields = ['status', 'add_time']

        def create(self, validated_data, **kwargs):
            user = validated_data.pop('user')
            coord = validated_data.pop('coord')
            level = validated_data.pop('level')
            images = validated_data.pop('images')

            user, created = User.objects.get_or_create(**user)

            coord = Coords.objects.create(**coord)
            level = DifficultyLevel.objects.create(**level)
            mount = AddMount.objects.create(**validated_data, user=user, coord=coord, level=level, status='new')


            for image in images:
                data = image.pop('image')
                title = image.pop('title')
                Images.objects.create(image=data, mount=mount, title=title)

            return mount

