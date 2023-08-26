from django.urls import path
from .views import Home, ProfileList


app_name = "netflixapp"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path("profiles/", ProfileList.as_view(), name="profile-list"),
]