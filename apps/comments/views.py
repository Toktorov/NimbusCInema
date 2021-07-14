from django.shortcuts import render, redirect
from apps.movies.models import Movie
from apps.comments.models import Comment


def comment_index(request, id):
    movie_object = Movie.objects.get(id=id)
    comments = movie_object.comment.all()
    return render(request, 'comments/index.html', {"comments": comments})


def update_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get("text")
        comment.text = text
        comment.save()
        return redirect('data')
    return render(request, 'comments/update.html')


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('data')
    return render(request, 'comments/delete.html')