from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(slug=slug)

        if queryset.exists():
            post = queryset.first()  # Get the first (and only) item in the queryset
            return render(
                request,
                "post_detail.html",
                {
                    "post": post,
                }
            )
        else:
            return HttpResponse("Post not found", status=404)
