from django.contrib import admin
from .models import Comments, Review, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'bio',
        'role',
        'email')
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'
    list_editable = ('role',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title_id',
        'author',
        'score',
        'pub_date'
    )


admin.site.register(Comments)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User, UserAdmin)
