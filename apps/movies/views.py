from django.shortcuts import render, redirect
from apps.movies.models import Movie, MovieImage, Like
from apps.movies.forms import MovieForm, MovieImageForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Movie.objects.filter(Q(title__icontains=key) |
                                    Q(description__icontains=key))
    return render(request, 'movie/index.html', {'movies': movies})

def detail(request, id=id):
    movies = Movie.objects.get(id=id)
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, movie=movies)
            like.delete()
        except:
            Like.objects.create(user=request.user, movie=movies)
    return render(request, 'movie/detail.html', {"movie": movies})

def create(request):
    form = MovieForm(request.POST, None)
    MovieImageFormset = inlineformset_factory(Movie, MovieImage, form=MovieImageForm, extra=1)
    if form.is_valid():
        movie = form.save()
        formset = MovieImageFormset(request.POST, request.FILES, instance=movie)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = MovieImageFormset()
    return render(request, 'movie/create.html', locals())

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        en_title = request.POST.get('en_title')
        description = request.POST.get('description')
        url_trailer = request.POST.get('url_trailer')
        file = request.FILES.get('file')
        movie_update = Movie.objects.get(id=id)
        movie_update.title = title
        movie_update.en_title = en_title
        movie_update.description = description
        movie_update.url_trailer = url_trailer
        movie_update.image = file
        movie_update.save()
        return redirect('index')
    return render(request, 'movie/update.html')

def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('index')
    return render(request, 'movie/delete.html')