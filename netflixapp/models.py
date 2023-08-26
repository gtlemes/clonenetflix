from django.db import models
from django.contrib.auth.models import AbstractUser
from netflixapp.choices import AGE_CHOICES, MOVIE_CHOICES
import uuid


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)
    
    
class Profile(models.Model):
    name = models.CharField("Nome", max_length=1000)
    age_limit = models.CharField("Perfil", choices=AGE_CHOICES, max_length=10) 
    uuid = models.UUIDField("id", default=uuid.uuid4)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField("Título",max_length=100)
    description = models.TextField("Descrição")
    created = models.DateTimeField(auto_now_add=True)
    classification = models.CharField("Tipo", choices=MOVIE_CHOICES, max_length=50)
    genre = models.CharField("Gênero", max_length=250)
    video = models.ManyToManyField("Video")
    image = models.ImageField("Capa", upload_to="images")
    age_limit = models.CharField("faixa etária", choices=AGE_CHOICES, max_length=10)
    uuid = models.UUIDField("id", default=uuid.uuid4)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField("Título", max_length=100)
    file = models.FileField("Arquivo", upload_to="files")
    
    def __str__(self):
        return self.title