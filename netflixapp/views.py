import imp
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie, MovieList as Movieslist
import re


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("netflixapp:profile-list")
        return render(request, "interface/index.html")



class Login(View):
    pass


class Signup(View):
    pass

method_decorator(login_required, name="dispatch")
class Logout(View):
    def logout(self, request):
        logout(request)
        return redirect("account/logout.html")



method_decorator(login_required, name="dispatch")
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {
            "profiles": profiles
        }
        return render(request, "profile/profilelist.html", context)

method_decorator(login_required, name="dispatch")
class ProfileManage(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {
            "profiles": profiles
        }
        return render(request, "profile/manageprofile.html", context)


method_decorator(login_required, name="dispatch")
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            "form": form
        }
        return render(request, "profile/profilecreate.html", context)
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, request.FILES or None)
        if form.is_valid():
            avatar = request.FILES.get('avatar')
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('netflixapp:profile-list')
            if avatar:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.avatar = avatar
                profile.save()
                return redirect("netflixapp:profile-list")
        
        context = {
            "form": form
        }
        return render(request, "profile/profilecreate.html", context)
    

class EditProfile(View):
    def get(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.get(uuid=profile_id)
        form = ProfileForm(instance=profile)
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'profile/editprofile.html', context)

    def post(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.get(uuid=profile_id)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('netflixapp:profile-list')
        context = {
            'profile': profile,
            'form': form,
        }
        return render(request, 'profile/editprofile.html', context)

class DeleteProfile(View):
    def post(self, request, profile_id, *args, **kwargs):
        profile = Profile.objects.get(uuid=profile_id)
        profile.delete()
        return redirect('netflixapp:profile-list')