from django.contrib import admin
from .models import Categories, Comments, Genres, Review, Title, TitleGenre, User


# class CategorisAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name, ')}


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'review',
        'text',
        'pub_date',
        'author'
    )


class GenresAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year')
    list_filter = ('year', 'genre', 'category')
    search_fields = ('name', 'description')


class TitleGenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'genre_id',
        'title_id'
    )


class RewiewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_id',
        'author',
        'score',
        'pub_date'
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'bio',
        'role',
        'email'
    )
    search_fields = ('username', )
    list_filter = ('username', )


# admin.site.register(Categories, CategorisAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(TitleGenre, TitleGenreAdmin)
admin.site.register(Review, RewiewAdmin)
admin.site.register(User, UserAdmin)
