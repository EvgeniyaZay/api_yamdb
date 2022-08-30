from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


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
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    username = models.CharField(
        max_length=150,
        unique=True,
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
        default=UserRole.USER.value,
        verbose_name='Роль'
    )
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    def __str__(self):
        return self.username
