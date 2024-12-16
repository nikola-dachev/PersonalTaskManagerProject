from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
class TaskListView(ListView):
    pass

class TaskCreateView(CreateView):
    pass

class TaskDetailView(DetailView):
    pass


class TaskUpdateView(UpdateView):
    pass

class TaskDeleteView(DeleteView):
    pass

class TaskUpdateCompleteView(UpdateView):
    pass


class TaskListOverDueView(ListView):
    pass


class TaskListCompletedView(ListView):
    pass



