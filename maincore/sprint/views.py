from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer, CoordsSerializer, AddMountSerializer, DifficultyLevelSerializer, ImageSerializer
from .models import User, Coords, DifficultyLevel, Images, AddMount


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['surname', 'name', 'otc', 'email']


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class MountViewSet(viewsets.ModelViewSet):
    queryset = AddMount.objects.all()
    serializer_class = AddMountSerializer

    def create(self, request, *args, **kwargs):
        if self.action == 'create':
            serializer = AddMountSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Успех!',
                        'id': serializer.instance.pk,
                    }
                )

            if status.HTTP_400_BAD_REQUEST:
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Некорректный запрос',
                        'id': None,
                    }
                )

            if status.HTTP_500_INTERNAL_SERVER_ERROR:
                return Response(
                    {
                        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': 'Ошибка при выполнении операции',
                        'id': None,
                    }
                )
        return super().create(request, *args, **kwargs)
