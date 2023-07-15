from  django.urls import path
from .views import PostListView,PostDetail

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetail.as_view(),name='post-detail'),

]