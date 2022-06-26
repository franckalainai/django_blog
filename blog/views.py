from django.views.generic import ListView, DetailView, CreateView
from . models import Post
from . forms import PostForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name: 'blog/post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'