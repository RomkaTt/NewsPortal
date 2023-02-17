from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .filters import PostFilter
from .forms import NewsForm, ArticleForm


class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.type_post = 'NE'
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        if news.type_post == 'NE':
            return super().form_valid(form)
    success_url = reverse_lazy('post_list')


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'post_search.html'
    context_object_name = 'post_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_number'] = Post.objects.all()
        context['filterset'] = self.filterset
        return context


class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type_post = 'AR'
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        if article.type_post == 'AR':
            return super().form_valid(form)
    success_url = reverse_lazy('post_list')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
