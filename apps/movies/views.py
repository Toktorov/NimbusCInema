from django.shortcuts import render, redirect
from apps.movies.models import Movie, MovieImage
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
    return render(request, 'movie/detail.html', {"movie": movies})

def create(request):
    form = MovieForm(request.POST or None)
    MovieImageFormSet = inlineformset_factory(Movie, MovieImage, form=MovieImageForm, extra=1)
    if request.method == 'POST' and user is staff:
        if form.is_valid():
            movie = Movie()
            movie.user = request.user
            movie.title = form.cleaned_data['title']
            movie.en_title = form.cleaned_data['en_title']
            movie.description = form.cleaned_data['description']
            movie.url_trailer = form.cleaned_data['url_trailer']
            movie.save()
            formset = MovieImageFormSet(request.POST, request.FILES, instance=movie)
            if formset.is_valid():
                formset.save()
            return redirect('index')
    formset = MovieImageFormSet()
    return render(request, 'movie/create.html', locals())

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        movie_update = Movie.objects.get(id=id)
        movie_update.title = title
        movie_update.description = description
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