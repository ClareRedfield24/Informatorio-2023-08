from django.urls import path
from .views import PostListView, PostDetailView

app_name = "apps.post"

urlpatterns = [
    path("posts/",PostListView.as_view(), name ="posts"),
    path("posts/<int:id>/", PostDetailView.as_view(), name= "post_individual"),
    
]