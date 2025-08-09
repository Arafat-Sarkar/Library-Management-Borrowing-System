from django.contrib import admin
from .models import BookModel, AuthorModel

admin.site.register(BookModel)
admin.site.register(AuthorModel)