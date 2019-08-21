from django.urls import path

from .views import PostView, BlogView
from . import views

urlpatterns = [
    path('tarot-theory/', views.theory, name='theory'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:post_id>', PostView.as_view()),
    # the following are my own personal blog views for midwestmagus, remove for initial release on github
    path('', views.index, name='index'),
]

