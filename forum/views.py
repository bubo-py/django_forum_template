from .models import ForumThread
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddThreadForm
from django.contrib.auth.decorators import login_required


def index(request):
    template = 'forum/index.html'
    threads = ForumThread.objects.all().order_by('-date_posted')[:6]
    return render(request, template, {'threads': threads})


def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, pk=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})


@login_required
def add_thread(request):
    if request.method == 'POST':
        form = AddThreadForm(request.POST)
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
