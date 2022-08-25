from django.db import models
from enum import Enum

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator

from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user


class UserRole(Enum):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    @staticmethod
    def get_max_lenght():
        max_lenght = max(len(role.value) for role in UserRole)
        return max_lenght

    @staticmethod
    def get_all_roles():
        return tuple((r.value, r.name) for r in UserRole)


class User(AbstractUser):
    USERNAME_VALIDATOR = RegexValidator(r'^[\w.@+-]+\z')
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    username = models.CharField(
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True
    )
    password = models.CharField(
        max_length=100,
        blank=True
    )
    confirmation_code = models.CharField(
        max_length=105,
        default='000000'
    )
    role = models.CharField(
        max_length=UserRole.get_max_lenght(),
        choices=UserRole.get_all_roles(),
        default=UserRole.USER.value
    )
    objects = UserManager()

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Categories(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Жанр', )
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Произведение')
    year = models.CharField(max_length=4,
                            verbose_name='Год издания')
    category = models.ForeignKey(Categories,
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 verbose_name='Произведение',
                                 null=True,
                                 )
    genre = models.ManyToManyField(Genres,
                                   through='TitleGenre',
                                   on_delete=models.SET_NULL,
                                   related_name='titles',
                                   verbose_name='Жанр',
                                   null=True
                                   )
    description = models.CharField(max_length=256,
                                   verbose_name='Описание')
    reviews = models.ForeignKey('Reviews',
                                on_delete=models.CASCADE,
                                related_name='titles',
                                verbose_name='Ревью',
                                null=True)

    class Meta:
        verbose_name = 'Произведение'
        constraints = [
            models.UniqueConstraint(
                fields=('genre', 'category'),
                name='unique_title'
            ),
        ]

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.genre}, {self.title}'


class Reviews(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Выберите значение от 1 до 10'),
            MaxValueValidator(10, 'Выберите значение от 1 до 10')
        ]
    )

    class Meta:
        verbose_name = 'Отзыв'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]

    def __str__(self):
        return f'Произведение: {self.title}, отзыв: "{self.text}".'


class Comments(models.Model):
    review = models.ForeignKey(
        Reviews,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Комментарий к отзыву',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Комментарий к отзыву'

    def __str__(self):
        return f'Отзыв: {self.review}, комментарий к отзыву: "{self.text}".'
