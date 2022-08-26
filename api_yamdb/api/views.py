from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .serializers import (CategoriesSerializers,
                          GenreSerializer,
                          TitleSerializer,
                          CommentSerializer,
                          ReviewSerializer,
                          UserSerializers
                          )
from reviews.models import Genres, Categories, Title, User, Reviews
from .permissions import (
    AdminOrReadOnly,
    IsAdmin,
    IsAdminOrIsModeratorOwnerOrReadOnly
)
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter)
    search_fields = ('=name')
    pagination_class = PageNumberPagination
    lookup_field = 'name'


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter)
    search_fields = ('=name')
    pagination_class = PageNumberPagination
    lookup_field = 'name'


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = (AdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    pagination_class = PageNumberPagination
    lookup_field = 'name'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['=username']
    pagination_class = PageNumberPagination
    permission_classes = [IsAdmin]
    lookup_field = 'username'

    # @api_view(['GET', 'PATCH'])


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrIsModeratorOwnerOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get("title_id"))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrIsModeratorOwnerOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Reviews, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Reviews, pk=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)
