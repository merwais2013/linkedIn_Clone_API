from django.urls import path
from .views import PostView, PostListView, CommentView, LikeView

urlpatterns = [
  path('post/', PostView.as_view()),
  path('post/<int:post_pk>/', PostView.as_view()),
  path('post-list/', PostListView.as_view()),
  path('post/<int:post_pk>/comments/', CommentView.as_view()),
  path('post/<int:post_pk>/likes/', LikeView.as_view()),
]