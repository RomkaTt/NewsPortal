from django.urls import path
from .views import PostList, ArticleCreate, ArticleUpdate, ArticleDelete, PostDetail

urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]