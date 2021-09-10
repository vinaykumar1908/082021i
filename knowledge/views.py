from django.shortcuts import get_object_or_404, redirect, render
from knowledge.models import KPost, KComment
from knowledge.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


@login_required
def homeView(request):
    return render(request, 'success.html')


@login_required
def home(request):
    context = {
        'posts': KPost.objects.all().order_by('-date_posted')
    }
    return render(request, 'knowledge/home.html', context)


class PostListView(ListView):
    model = KPost
    template_name = "knowledge/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = KPost
    template_name = 'knowledge/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return KPost.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = KPost
    context_object_name = 'post'
    template_name = 'knowledge/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = KPost
    fields = ['title', 'content', 'upload']
    template_name = 'knowledge/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = KPost
    fields = ['title', 'content', 'upload']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = KPost
    success_url = '/Contracts/'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def add_comment_to_post(request, pk):
    post = get_object_or_404(ContractPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.approve()
            comment.save()
            return redirect('kpost-detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'knowledge/add_comment_to_post.html', {'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(ContractComment, pk=pk)
    comment.delete()
    return redirect('kpost-detail', pk=comment.post.pk)
