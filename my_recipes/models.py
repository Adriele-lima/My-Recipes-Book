from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    featured_image = CloudinaryField('featured_image', default='placeholder')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_on = models.DateTimeField(auto_now=True)
    ingredients_content = models.TextField()
    method_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
