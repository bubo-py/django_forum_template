from .models import ForumThread
from django.shortcuts import render, get_object_or_404
from .forms import AddThreadForm


def index(request):
    template = 'forum/index.html'
    return render(request, template)


def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, pk=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})


def add_thread(request):
    form = AddThreadForm(request.POST)

    thread = form.save(commit=False)
    thread.author = request.user
    thread.save()

    context = {'form': form}
    return render(request, 'forum/add_thread.html', context)
