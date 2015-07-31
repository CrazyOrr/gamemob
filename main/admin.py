from django.contrib import admin

from .models import Game, Company, Person, Platform, Genre, Mode, ReleaseDate


# Register your models here.
admin.site.register(Game)
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Platform)
admin.site.register(ReleaseDate)
admin.site.register(Genre)
admin.site.register(Mode)
