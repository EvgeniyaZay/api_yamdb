from rest_framework import serializers
from reviews.models import Comments, Reviews
from reviews.models import Categories, Genres, Title


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comments
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    pass