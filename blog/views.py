from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .models import Post, PostCategory
from .forms import PostSearchForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    form_class = PostSearchForm

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Post.objects.filter(title__icontains=query, is_published=True)
        else:
            return Post.objects.filter(is_published=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['form'] = self.form_class(self.request.GET)
        context['q'] = self.request.GET.get('q', '')
        return context  

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

class PostIndexView(ListView):
    template_name= 'blog/post_index.html'
    context_object_name = 'categories'
    form_class = PostSearchForm

    def get_queryset(self):
        return PostCategory.objects.filter(post__isnull=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        categories = context['categories']
        context['categories_with_posts'] = [
            {'category': category, 'posts': Post.objects.filter(categories=category, is_published=True)}
            for category in categories
        ]
        return context
    
class PostCreateView(CreateView):
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    model = Post
    fields = ['title', 'content', 'thumbnail', 'word_count', 'reading_time', 'categories', 'is_published']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class PostUpdateView(UpdateView):
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    model = Post
    fields = ['title', 'content', 'thumbnail', 'word_count', 'reading_time', 'categories', 'is_published']

class PostDeleteView(DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    model = Post         
    
class PostContentView(ListView):
    model = Post
    template_name = 'blog/post_content.html'
    context_object_name = 'posts'
    form_class = PostSearchForm
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('query', '')
        if q:
            return Post.objects.filter(title__icontains=q, is_published=True)
        else:
            return Post.objects.filter(is_published=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        context['query'] = self.request.GET.get('query', '')
        posts = context['posts']

        paginator = Paginator(posts, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            paginated_posts = paginator.page(page)
        except PageNotAnInteger:
            paginated_posts = paginator.page(1)
        except EmptyPage:
            paginated_posts = paginator.page(paginator.num_pages)

        context['paginated_posts'] = paginated_posts
        return context  

class PostSearchView(View):
    template_name = 'blog/post_search.html'

    def get(self, request, *args, **kwargs):
        form = PostSearchForm(request.GET)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostSearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data.get('query', '')
            # Redirect to the post content list with the search query
            return redirect('blog:post_content', query=q)
        return render(request, self.template_name, {'form': form})