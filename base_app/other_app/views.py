from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import GameForm
from .models import Game


def post_list(request):
    post = Game.objects.filter(release_date=timezone.now()).order_by('release_date')
    return render(request, 'other_app/index.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = GameForm()
    return render(request, 'other_app/add.html', {'form': form})
