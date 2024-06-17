from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.DiscussionCreateView.as_view()),
    path('comment/', views.CommentsCreateView.as_view()),
    path('list/', views.DiscussionListView.as_view()),
    path('<int:pk>/', views.DiscussionDetailView.as_view()),
    path('comment/list/', views.CommentsListView.as_view()),
    path('comment/detail/', views.CommentDetailView.as_view())
]