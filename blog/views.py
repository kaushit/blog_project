from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# ---------funcion_view--------------


def about(request):
    return render(request=request, template_name='blog/about.html')

# --------class_view-----------------


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 4


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))

        if self.request.user == post.author:
            return True
        else:
            return False


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    paginate_by = 3
    context_object_name = 'post'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
