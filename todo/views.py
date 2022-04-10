from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Todo
# Create your views here.

class TodoList(ListView):

    model = Todo
    context_object_name = 'tasks'
    

class TodoDetail(DetailView):

    model = Todo
    context_object_name = 'task'


class TodoCreate(CreateView):

    model = Todo
    # 入力したい値　　
    fields = ['title', 'description', 'deadline']
    # 作成出来たらリダイレクトする場所
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):

    model =Todo
    fields = ['title', 'description', 'deadline']
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):

    model = Todo
    context_object_name = 'tasks'
    success_url = reverse_lazy('list')
