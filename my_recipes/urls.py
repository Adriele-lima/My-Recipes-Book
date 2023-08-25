from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('create_recipe/', views.PostDetail.create_recipe, name='create_recipe'),
    path('edit/<slug>/', views.PostDetail.edit_recipe, name='edit_recipe'),
    path('delete/<slug>/', views.PostDetail.delete_recipe, name='delete_recipe'),
]
