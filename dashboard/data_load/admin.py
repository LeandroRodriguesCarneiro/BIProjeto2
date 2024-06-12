from django.contrib import admin
from .models import Genre, Platform, Publisher, Game

admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Game)
