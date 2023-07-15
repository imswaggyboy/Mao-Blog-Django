from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('', views.PostListView.as_view(), name='post_list'),
    # path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/<int:pk>/', views.post_details, name='post_detail'),
    path('like/<int:pk>/', views.like_post, name='like_post'),


    path('<int:year>/<int:month>/<int:day>/<slug:slug>/<int:pk>/update/',
          views.PostUpdateView.as_view(),
            name='post_update'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/<int:pk>/delete/',
          views.PostDeleteView.as_view(),
            name='post_delete'),
]