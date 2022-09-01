import datetime

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from user.models import User


SLUG_VALIDATOR = RegexValidator(r'^[-a-zA-Z0-9_]+$')


class Categories(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Категория'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        validators=[SLUG_VALIDATOR]
    )

    class Meta:
        verbose_name = 'Жанр',
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Произведение'
    )
    year = models.IntegerField(
        verbose_name='Год издания',
        validators=[MaxValueValidator(datetime.datetime.now().year)]
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Произведение',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genres,
        through='TitleGenre',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre}, {self.title}'


class Review(models.Model):
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
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Выберите значение от 1 до 10'),
            MaxValueValidator(10, 'Выберите значение от 1 до 10')
        ]
    )

    class Meta:
        verbose_name = 'Отзыв'
        ordering = ['pub_date']
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
        Review,
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
        ordering = ['pub_date']

    def __str__(self):
        return f'Отзыв: {self.review}, комментарий к отзыву: "{self.text}".'
