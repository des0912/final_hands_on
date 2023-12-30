from abc import update_abstractmethods
import copy
from doctest import Example
import html
from msilib.schema import AdminExecuteSequence
from os import path
from django import template
from django.shortcuts import render
from manage import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'exam_app/post_list.html', {'posts': posts})
update_abstractmethods.your-template/Example.app/post_list.html
html
copy.code
{"% extends 'base.html' %"}

{"% block title %}Post List{% endblock %"}

{"% block content %"}
  <h2>Posts</h2>
  {"% for post in posts %"}
    <div class="card mb-3">
      <div class="card-body">
        <p>{{ post.content }}</p>
        <p>Author: {{ post.user_profile.user.username }}</p>
        {"% if post.image %"}
          <img src="{{ post.image.url }}" class="img-fluid" alt="{{ post.user_profile.user.username }}'s post">
        {"% endif %"}
        <h4>Comments:</h4>
        <ul>
          {"% for comment in post.comment_set.all %"}
            <li>{{ comment.text }} - {{ comment.user_profile.user.username }}</li>
          {"% endfor %"}
        </ul>
        <h4>Likes:</h4>
        <ul>
          {"% for like in post.like_set.all %"}
            <li>{{ like.user_profile.user.username }}</li>
          {"% endfor %"}
        </ul>
      </div>
    </div>
  {"% endfor %"}
{"% endblock %"}

urlpatterns = [
    path('admin/', AdminExecuteSequence.site.urls),
    path('posts/', post_list, name='post_list'),
]