from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Categories, Genre, Title


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    pass