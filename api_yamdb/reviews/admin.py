from django.contrib import admin
from .models import Comments, Review, User


admin.site.register(Comments)
admin.site.register(Review)
admin.site.register(User)
