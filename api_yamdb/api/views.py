from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .serializers import (CategoriesSerializers,
                          GenreSerializer,
                          TitleSerializer,
                          CommentSerializer,
                          ReviewSerializer,
                          UserSerializers
                          )
from reviews.models import Genre, Categories, Title, User
from .permissions import AdminOrReadOnly, IsAdmin
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from reviews.models import Reviews, Title



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
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = (filters.SearchFilter)
    search_fields = ('=username')
    pagination_class = PageNumberPagination
    permission_classes = [IsAdmin]
    lookup_field = 'username'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        # Получаем произведение по id из эндпоинта
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        # возвращаем все отзывы для найденного произведения
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Reviews, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Reviews, pk=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)
