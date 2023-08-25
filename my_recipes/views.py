from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse
from .models import Post
from .forms import RecipeForm


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

    def create_recipe(request):
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')

        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create_recipe.html', context)

    def edit_recipe(request, slug):
        item = get_object_or_404(Post, slug=slug)
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('home')

        form = RecipeForm(instance=item)
        context = {
            'form': form
        }
        return render(request, 'edit_recipe.html', context)

    def delete_recipe(request, slug):
        item = get_object_or_404(Post, slug=slug)
        item.delete()
        return redirect('home')
