from rest_framework import serializers
from reviews.models import Categories, Genres, Title, Comments, User, Review
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from reviews.models import UserRole


class UserSerializers(serializers.ModelSerializer):
    username = serializers.RegexField(regex=r'[\w.@+-]+\Z', max_length=150)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.CharField(max_length=254)
    role = serializers.ChoiceField(
        choices=UserRole.get_all_roles(),
        default=UserRole.USER.value,
        required=False
    )

    def validate_username(self, username):
        if User.objects.filter(
            username=username
        ).exists():
            raise serializers.ValidationError(
                'Пользователь с таким именем уже существует'
            )
        return username

    def validate_email(self, email):
        if User.objects.filter(
            email=email
        ).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует'
            )
        return email

    class Meta:
        fields = (
            'bio',
            'username',
            'first_name',
            'last_name',
            'email',
            'role')
        model = User


class GetCodeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" запрещено!'
            )
        return username

    class Meta:
        fields = ("username", "email")
        model = User


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=Genres.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'category',
            'genre',
            'description',
            'rating',
        )


class ReadOnlyTitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True)
    category = CategoriesSerializers()

    class Meta:
        model = Title
        fields = '__all__'

    def get_rating(self, obj):
        return obj.score


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
            if Review.objects.filter(
                    title=title,
                    author=request.user
            ).exists():
                raise ValidationError(
                    'На одно произведение можно оставить только один отзыв!'
                )
        return data

    class Meta:
        model = Review
        fields = '__all__'
