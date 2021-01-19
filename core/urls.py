from django.urls import path
from .views import PostView, TestView, RegisterView

urlpatterns = [
    path(r'', TestView.as_view(), name = "Test View"),
    path(r'post/', PostView.as_view(), name = 'Post View'),
    path(r'api/register/', RegisterView.as_view(), name = 'Register'),
]