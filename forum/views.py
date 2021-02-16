from .models import ForumThread
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddThreadForm


def index(request):
    template = 'forum/index.html'
    return render(request, template)


def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, pk=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})


def add_thread(request):
    if request.method == 'POST':
        form = AddThreadForm(request.POST)
        form.author = request.user
        if form.is_valid():
            # this saves the thread but doesn't commit to db
            form = form.save(commit=False)
            form.author = request.user  # set logged user as an author and then save
            form.save()
            return redirect('index')

    else:
        form = AddThreadForm()

    context = {'form': form}
    return render(request, 'forum/add_thread.html', context)
