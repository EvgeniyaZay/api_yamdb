from rest_framework import viewsets
from .serializers import (CategoriesSerializers,
                          GenreSerializer,
                          TitleSerializer)
from reviews.models import Genre, Categories, Title
from .permissions import AdminOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = LimitOffsetPagination


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = (AdminOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    pass
