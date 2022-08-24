from rest_framework import serializers
from reviews.models import Categories, Genres, Title
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    pass