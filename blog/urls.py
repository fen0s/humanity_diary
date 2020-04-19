from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path("posts", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="detail_post"),
    path("submit", views.submit_view, name="submit")
]