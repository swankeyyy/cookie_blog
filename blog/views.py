from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")) #в модели поста есть категория и обращаюсь к ее слагу

def home(request):
    return render(request, 'base.html')
