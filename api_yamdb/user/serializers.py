from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, UserRole


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
