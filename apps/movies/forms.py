from django import forms
from apps.movies.models import Movie, MovieImage
from django.forms import ModelForm


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'en_title', 'description', 'trailer', 'film', 'year', 'country', 'director', 'actors' ]

class MovieImageForm(forms.ModelForm):
    class Meta:
        model = MovieImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }