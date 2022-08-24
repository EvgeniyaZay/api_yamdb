from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from reviews.models import Reviews, Title
from .serializers import (
    CommentSerializer,
    ReviewSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    pass


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
