from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()
        
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
        return PostCategory.objects.filter(post__isnull=False).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        categories = context['categories']
        context['categories_with_posts'] = [
            {'category': category, 'posts': Post.objects.filter(categories=category)}
            for category in categories
        ]
        return context
    
class PostContentView(ListView):
    model = Post
    template_name = 'blog/post_content.html'
    context_object_name = 'posts'
    form_class = PostSearchForm
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('query', '')
        if q:
            return Post.objects.filter(title__icontains=q)
        else:
            return Post.objects.all()
        
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