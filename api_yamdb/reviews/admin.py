from django.contrib import admin
from .models import Comments, Reviews, User

admin.site.register(Comments)
admin.site.register(Reviews)
admin.site.register(User)
