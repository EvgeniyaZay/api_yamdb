from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 related_name='titles',
                                 )
    genre = models.ForeignKey(Genres,
                              on_delete=models.CASCADE,
                              related_name='genres',
                              )

    def __str__(self):
        return self.name


class UserModel(models.Model):
    pass
