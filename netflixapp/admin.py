from django.contrib import admin
from netflixapp.models import CustomUser, Profile, Movie, Video


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "classification", "genre", "age_limit")


admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Video)

