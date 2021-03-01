from .models import ForumThread
# from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddThreadForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


class ThreadListView(ListView):
    model = ForumThread
    template_name = 'forum/index.html'
    context_object_name = 'threads'
    ordering = '-date_posted'
    paginate_by = 5


class ThreadDetailView(DetailView):
    model = ForumThread
    context_object_name = 'thread'


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
