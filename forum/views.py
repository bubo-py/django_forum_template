from .models import ForumThread
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddThreadForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


class ThreadListView(ListView):
    model = ForumThread
    template_name = 'forum/index.html'
    context_object_name = 'threads'
    ordering = '-date_posted'
    paginate_by = 5


class ThreadDetailView(DetailView):
    model = ForumThread
    context_object_name = 'thread'


class OneUserThreadsView(ListView):
    model = ForumThread
    template_name = 'forum/one_user_threads.html'
    context_object_name = 'threads'
    ordering = '-date_posted'

    def get_queryset(self):
        u = get_object_or_404(User, username=self.kwargs.get('username'))
        return ForumThread.objects.filter(author=u)


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
