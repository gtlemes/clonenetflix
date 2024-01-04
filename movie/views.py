from django.shortcuts import redirect, render, get_object_or_404
from netflixapp.models import Profile, Movie, MovieList as Movieslist
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


method_decorator(login_required, name="dispatch")
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.all()
            popular_movies = movies.filter(highlighted=True)
            releases = movies.filter(release=True)

            tv_shows = movies.filter(genre__genre="Programas de TV")

            action = Movie.objects.filter(genre__genre="Ação")
            adventure = Movie.objects.filter(genre__genre="Aventura")
            action_adventure = action.intersection(adventure)

            animations = movies.filter(classification="Kids")

            if profile not in request.user.profiles.all():
                return redirect("netflixapp:profile-list")
            
            context = {
                "movies": movies,
                "popular_movies": popular_movies,
                "releases": releases,
                "tv_shows": tv_shows,
                "action_adventure": action_adventure,
                "animations": animations
            }

            return render(request, "movies/movielist.html", context)
        
        except Profile.DoesNotExist:
            return redirect("netflixapp:profile-list")


method_decorator(login_required, name="dispatch")
class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)

            context = {
                "movie": movie
            }

            return render(request, "movies/moviedetail.html", context)

        except Movie.DoesNotExist:
            return redirect("netflxapp:profile-list")
        
method_decorator(login_required, name="dispatch")
class PlayMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()

            context = {
                "movie": list(movie)
            }

            return render(request, "movies/playmovie.html", context)
        
        except Movie.DoesNotExist:
            return redirect("netflixapp:profile-list")
        
        
method_decorator(login_required, name="dispatch")
class MoviesAll(View):
    def get(self, request, *args, **kwargs):
        trending_movie = Movie.objects.filter(classification="Movies", trending=True)
        action = Movie.objects.filter(classification="Movies", genre__genre="Ação")
        adventure = Movie.objects.filter(classification="Movies", genre__genre="Aventura")
        comedy = Movie.objects.filter(classification="Movies", genre__genre="Comédia")
        adolescent = Movie.objects.filter(classification="Movies", genre__genre="Adolescente")
        sc_fic = Movie.objects.filter(classification="Movies", genre__genre="Ficção Científica")
        classic = Movie.objects.filter(classification="Movies", genre__genre="Clássicos")
        terror = Movie.objects.filter(classification="Movies", genre__genre="Terror")
        war = Movie.objects.filter(classification="Movies", genre__genre="Guerra")
        romance = Movie.objects.filter(classification="Movies", genre__genre="Romance")
        thriller = Movie.objects.filter(classification="Movies", genre__genre="Suspense")
        mystery = Movie.objects.filter(classification="Movies", genre__genre="Mistério")
        drama = Movie.objects.filter(classification="Movies", genre__genre="Drama")
        crime = Movie.objects.filter(classification="Movies", genre__genre="Crime")
        historical = Movie.objects.filter(classification="Movies", genre__genre="Histórico"),
        documentaries = Movie.objects.filter(classification="Movies", genre__genre="Documentários")
        musical = Movie.objects.filter(classification="Movies", genre__genre="Musicais")
        fantasy = Movie.objects.filter(classification="Movies", genre__genre="Fantasia")

        action_adventure = action.intersection(adventure)
        adventure_comedy = adventure.intersection(comedy)
        terror_comedy = terror.intersection(comedy)

        
        context = {
            "trending_movie": trending_movie,
            "action_adventure": action_adventure,
            "action": action,
            "adventure": adventure,
            "comedy": comedy,
            "adolescent": adolescent,
            "sc_fic": sc_fic,
            "classic": classic,
            "terror": terror,
            "war": war,
            "romance": romance,
            "thriller": thriller,
            "mystery": mystery,
            "drama": drama,
            "crime": crime,
            "historical": historical,
            "documentaries": documentaries,
            "musical": musical,
            "fantsy": fantasy,
            "adventure_comedy": adventure_comedy,
            "terror_comedy": terror_comedy
        }

        return render(request, "interface/movies.html", context)

method_decorator(login_required, name="dispatch")
class SeriesAll(View):
    def get(self, request, *args, **kwargs):
        trending_series = Movie.objects.filter(classification="Series", trending=True)
        action = Movie.objects.filter(classification="Series", genre__genre="Ação")
        adventure = Movie.objects.filter(classification="Movies", genre__genre="Aventura")
        comedy = Movie.objects.filter(classification="Series", genre__genre="Comédia")
        sc_fic = Movie.objects.filter(classification="Series", genre__genre="Ficção Científica")
        adolescent = Movie.objects.filter(classification="Series", genre__genre="Adolescente")
        romance = Movie.objects.filter(classification="Series", genre__genre="Romance")
        documentaries = Movie.objects.filter(classification="Series", genre__genre="Documentários")
        mystery = Movie.objects.filter(classification="Series", genre__genre="Mistério")
        drama = Movie.objects.filter(classification="Series", genre__genre="Drama")
        crime = Movie.objects.filter(classification="Series", genre__genre="Crime")
        soap_operas = Movie.objects.filter(classification="Series", genre__genre="Novelas")
        tv_shows = Movie.objects.filter(classification="Series", genre__genre="Programas de TV")
        historical = Movie.objects.filter(classification="Series", genre__genre="Histórico")
        fantasy = Movie.objects.filter(classification="Series", genre__genre="Fantasia")
        police = Movie.objects.filter(classification="Series", genre__genre="Policial")
        thriller = Movie.objects.filter(classification="Series", genre__genre="Suspense")
        terror = Movie.objects.filter(classification="Movies", genre__genre="Terror")

        
        action_adventure = action.intersection(adventure)
        action_drama = action.intersection(drama)
        police_crime = police.intersection(crime)
        scfic_fantasy = sc_fic.intersection(fantasy)
        terror_thriller = terror.intersection(thriller)



        context = {
            "trending_series": trending_series,
            "action": action,
            "comedy": comedy,
            "sc_fic": sc_fic,
            "adolescent": adolescent,
            "romance": romance,
            "documentaries": documentaries,
            "mystery": mystery,
            "drama": drama,
            "soap_operas": soap_operas,
            "tv_shows": tv_shows,
            "historical": historical,
            "fantasy": fantasy,
            "terror_thriller": terror_thriller,
            "action_adventure": action_adventure,
            "action_drama": action_drama,
            "police_crime": police_crime,
            "scfic_fantasy": scfic_fantasy,
        }

        return render(request, "interface/series.html", context)
    

method_decorator(login_required, name="dispatch")
class AnimationsAll(View):
    def get(self, request, *args, **kwargs):
        trending_kids = Movie.objects.filter(classification="Kids", trending=True)
        action = Movie.objects.filter(classification="Kids", genre__genre="Ação")
        adventure = Movie.objects.filter(classification="Kids", genre__genre="Aventura")
        comedy = Movie.objects.filter(classification="Kids", genre__genre="Comédia")
        fantasia = Movie.objects.filter(classification="Kids", genre__genre="Fantásia")
        animes = Movie.objects.filter(classification="Kids", genre__genre="Animes")
        animations = Movie.objects.filter(classification="Kids", genre__genre="Animação")
        musical = Movie.objects.filter(classification="Kids", genre__genre="Musicais")
        drama = Movie.objects.filter(classification="Kids", genre__genre="Drama")
        classics = Movie.objects.filter(classification="Kids", genre__genre="Clássicos")
        sc_fic = Movie.objects.filter(classification="Kids", genre__genre="Ficção Científica")
        family = Movie.objects.filter(classification="Kids", genre__genre="Família")


        action_adventure = action.intersection(adventure)


        context = {
            "trending_kids": trending_kids,
            "action_adventure": action_adventure,
            "action": action,
            "adventure": adventure,
            "comedy": comedy,
            "fantasia": fantasia,
            "animes": animes,
            "animations": animations,
            "musical": musical,
            "drama": drama,
            "classics": classics,
            "sc_fic": sc_fic,
            "family": family,
        }

        return render(request, "interface/animations.html", context)