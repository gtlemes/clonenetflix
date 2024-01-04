from django.urls import path
from .views import *
from . import views
from movie.views import MovieList


app_name = "netflixapp"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profiles/", ProfileList.as_view(), name="profile-list"),
    path("profiles/manage/", ProfileManage.as_view(), name="profile-manage"),
    path("profiles/create/", ProfileCreate.as_view(), name="profile-create"),
    path("watch/<str:profile_id>/", MovieList.as_view(), name="movie-list"),
    path('editprofile/<str:profile_id>/', EditProfile.as_view(), name='edit-profile'),
    path('deleteprofile/<uuid:profile_id>/', DeleteProfile.as_view(), name='delete-profile'),
]