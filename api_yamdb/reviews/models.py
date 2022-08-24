from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 related_name='titles',
                                 verbose_name='Произведение',
                                 )
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE,
                              related_name='genres',
                              )

    def __str__(self):
        return self.name


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



