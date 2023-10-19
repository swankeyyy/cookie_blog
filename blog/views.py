from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related(
            'category')  # в модели поста есть категория и обращаюсь к ее слагу
    # select_related обращается к связанной категории


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug' #т.к. определено в урлах адрес нестандартный <slug:post_slug>


def home(request):
    return render(request, 'base.html')
