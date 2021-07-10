from apps.movies.models import Movie, MovieImage
from django import forms


class MovieFrom(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'description']

class MovieImageForm(forms.ModelForm):
    class Meta:
        model = MovieImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }