from django.shortcuts import render
from apps.movies.models import *
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
class MovieIndexView(ListView):
    model = Movie
    template_name = 'movie/index.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/detail.html'

# class MovieCreateView(CreateView):
#     model = Movie
#     template_name = 'movie/create.html'

def create_movie(request):
    form = MovieForm(request.POST or None)
    MovieImageFormSet = inlineformset_factory(Movie, MovieImage, form=MovieImageForm, extra=1)
    if request.method == 'POST':
        if form.is_valid():
            movie = Movie()
            movie.title = form.cleaned_data['title']
            movie.description = form.cleaned_data['description']
            movie.save()
            formset = MovieImageFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()
            return redirect('index')
    formset = MovieImageFormSet()
    return render(request, 'movie/create.html', locals())
