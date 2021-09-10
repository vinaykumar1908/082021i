from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='kblogHome'),
    path('kuser/<str:username>', UserPostListView.as_view(), name='kuser-posts'),
    path('kpost/<int:pk>/', PostDetailView.as_view(), name='kpost-detail'),
    path('kpost/new/', PostCreateView.as_view(), name='kpost-create'),
    path('kpost/<int:pk>/update/', PostUpdateView.as_view(), name='kpost-update'),
    path('kpost/<int:pk>/delete/', PostDeleteView.as_view(), name='kpost-delete'),
    #path('success/', views.homeView, name='TestLink'),
    path('kpost/<int:pk>/comment/', views.add_comment_to_post,name='kadd_comment_to_post'),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('kcomment/<int:pk>/remove/', views.comment_remove, name='kcomment_remove'),

]
