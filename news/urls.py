from django.urls import path

from .views import PostList, PostDetail, NewsCreate, NewsUpdate, NewsDelete, PostSearch

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete')
]
