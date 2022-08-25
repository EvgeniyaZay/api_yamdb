from rest_framework import serializers
from reviews.models import Categories, Genres, Title, Comments, User, Reviews, TitleGenre


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('username',)
        model = User


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    category = CategoriesSerializers
    genre = GenreSerializer(many=True)

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        categories = validated_data.pop('category')
        title = Title.objects.create(**validated_data)
        if genres:
            for genre in genres:
                current_genre, status = Genres.objects.get_or_create(
                    **genre)
                TitleGenre.objects.create(
                    genre=current_genre, title=title)
        elif categories:
            for category in categories:
                current_category, status = Genres.objects.get_or_create(
                    **category)
                TitleGenre.objects.create(
                    category=current_category, title=title)
        return title

    class Meta:
        fields = '__all__'
        model = Title


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

    class Meta:
        model = Reviews
        fields = '__all__'

