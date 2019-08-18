from django.urls import path

from .views import PostView, BlogView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', BlogView.as_view()),
    path('blog/<int:post_id>', PostView.as_view()),
    path('about/', views.about, name='about'),
    # the following are my own personal blog views for midwestmagus, remove for initial release on github
    path('process/', views.process, name='process'),

]

