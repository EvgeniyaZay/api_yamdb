from rest_framework import serializers
from reviews.models import Categories, Genres, Title, Comments, User, Reviews, TitleGenre
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
import statistics


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ('username',)
        model = User


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    category = CategoriesSerializers
    genre = GenreSerializer(many=True)
    rating = serializers.SerializerMethodField()

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
        fields = ('name', 'year', 'rating', 'description', 'genres', 'category',)
        model = Title

    def get_rating(self, obj):
        return statistics.mean(obj.reviews.score)


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

    def validate(self, data):
        request = self.context['request']
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if request.method == 'POST':
            if Reviews.objects.filter(
                title=title,
                author=request.user
            ).exists():
                raise ValidationError(
                    'На одно произведение можно оставить только один отзыв!'
                )
        return data

    class Meta:
        model = Reviews
        fields = '__all__'
