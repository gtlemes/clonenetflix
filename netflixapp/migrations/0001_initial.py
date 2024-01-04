# Generated by Django 4.2.6 on 2023-12-09 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('classification', models.CharField(choices=[('Series', 'Séries'), ('Movies', 'Filmes'), ('Kids', 'Kids')], max_length=50, verbose_name='Classificação')),
                ('genre', models.CharField(choices=[('Action', 'Ação'), ('Action-Adventure', 'Ação e aventura'), ('Comedy', 'Comédia'), ('Adventure-Comedy', 'Aventura e comédia'), ('Science-Fiction', 'Ficção Científica'), ('Classic', 'Clássicos'), ('Terror', 'Terror'), ('Horror-thriller', 'Terror e Suspense'), ('Romance', 'Romance'), ('Thriller', 'Suspense'), ('Mystery', 'Mistério'), ('Documentaries', 'Documentários'), ('Drama', 'Drama'), ('Police', 'Policial'), ('Teenagers', 'Adolescentes'), ('Soap_operas', 'Novelas'), ('TV Shows', 'Programas de TV'), ('Animes', 'Animes'), ('Historical', 'Histórico'), ('Animations', 'Animações'), ('Musical', 'Musicais')], max_length=500, verbose_name='Gênero')),
                ('runtime', models.CharField(max_length=50, verbose_name='Duração')),
                ('cast', models.CharField(help_text='apenas os principais atores', max_length=250, verbose_name='Elenco')),
                ('release_year', models.CharField(max_length=10, verbose_name='Ano de lançamento')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='id')),
                ('highlighted', models.BooleanField(default=False, verbose_name='Popular')),
                ('release', models.BooleanField(default=False, verbose_name='Lançamento')),
                ('trending', models.BooleanField(default=False, verbose_name='Em Alta')),
                ('genretwo', models.ManyToManyField(blank=True, to='netflixapp.genre', verbose_name='Gêneros')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Nome')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='Avatar')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='id')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('file', models.FileField(upload_to='files', verbose_name='Arquivo de vídeo')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('file', models.FileField(blank=True, null=True, upload_to='files', verbose_name='Arquivo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Capa')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banners', verbose_name='Banner')),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflixapp.movie')),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.ManyToManyField(blank=True, to='netflixapp.trailer'),
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.ManyToManyField(blank=True, to='netflixapp.video'),
        ),
    ]
