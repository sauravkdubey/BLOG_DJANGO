from django.urls import path

from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import allposts, post_detail,logout_blog,post_new,register,login_blog,post_edit

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    path('', home, name='register'),
    # ex: /blog/skd
    path('<str:username>', home, name='login_blog'),
    # ex: /blog/post/5/
    path('post/<int:pk>/', PostView.as_view(), name='allposts'),
    # ex: /blog/post/create/
    path('post/create/', PostCreate.as_view(), name='post_detail'),
    # ex: /blog/post/5/update/
    path('post/create/<int:pk>/update', PostUpdate.as_view(), name='post_new'),
    # ex: /blog/post/5/delete/
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_edit'),
    # ex: /blog/post/5/comment/
    path('post/<int:pk>/comment/', CommentCreate.as_view(), name='logout_blog')
]
