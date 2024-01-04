from django.contrib import admin
from netflixapp.models import Profile, Movie, Video, Trailer, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "classification")


# admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Video)
admin.site.register(Trailer)
admin.site.register(Genre)
