from django.urls import path
from .views import *
from . import views
from netflixapp.views import *
from netflixapp.urls import *


app_name = "movie"

urlpatterns = [
    path("watch/detail/<str:movie_id>/", MovieDetail.as_view(), name="movie-detail"),
    path("watch/play/<str:movie_id>/", PlayMovie.as_view(), name="play-movie"),
    path("page/movies/", MoviesAll.as_view(), name="movies-all"),
    path("page/series/", SeriesAll.as_view(), name="series-all"),
    path("page/animations/", AnimationsAll.as_view(), name="animations-all"),

]