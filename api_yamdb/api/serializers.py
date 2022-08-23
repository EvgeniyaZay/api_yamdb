from rest_framework import serializers
from reviews.models import Categories, Genres, Title
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Categories, Genres, Title


class UserSerializer(serializers.ModelSerializer):
    pass