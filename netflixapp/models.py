from django.conf import settings
from django.db import models
from netflixapp.choices import MOVIE_CHOICES, GENRE_CHOICES
import uuid

# Profile


    
class Profile(models.Model):
    name = models.CharField("Nome", max_length=1000)
    avatar = models.ImageField("Avatar", upload_to="avatar", null=True, blank=True)
    uuid = models.UUIDField("id", default=uuid.uuid4)

    def __str__(self):
        return self.name

# Movie

class Genre(models.Model):
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.genre

class Video(models.Model):
    title = models.CharField("Título", max_length=100)
    file = models.FileField("Arquivo", upload_to="files", null=True, blank=True)
    image = models.ImageField("Capa", upload_to="images", null=True, blank=True)
    banner = models.ImageField("Banner", upload_to="banners", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Trailer(models.Model):
    title = models.CharField("Título", max_length=100)
    file = models.FileField("Arquivo de vídeo", upload_to="files")

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField("Título",max_length=100)
    description = models.TextField("Descrição")
    created = models.DateTimeField(auto_now_add=True)
    classification = models.CharField("Classificação", choices=MOVIE_CHOICES, max_length=50)
    # genre = models.CharField("Gênero", choices=GENRE_CHOICES, max_length=500)
    genre = models.ManyToManyField(Genre, verbose_name="Gêneros", blank=True)
    runtime = models.CharField("Duração", max_length=50)
    cast = models.CharField("Elenco", max_length=250, help_text="apenas os principais atores")
    release_year = models.CharField("Ano de lançamento", max_length=10)
    video = models.ManyToManyField(Video, blank=True)
    trailer = models.ManyToManyField(Trailer, blank=True)
    uuid = models.UUIDField("id", default=uuid.uuid4)
    highlighted = models.BooleanField(verbose_name=("Popular"), default=False)
    release = models.BooleanField(verbose_name=("Lançamento"), default=False)
    trending = models.BooleanField(verbose_name=("Em Alta"), default=False)

    def __str__(self):
        return self.title

class MovieList(models.Model):
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
