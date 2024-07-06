from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


urlpatterns = [
    path("sign-up", UserRegisterApiView.as_view(), name="register"),
    path("login", obtain_auth_token, name="token"),

    path("users", UserListAPIView.as_view(), name="users"),
    path("get-user", UserRetrieveAPIView.as_view(), name="user"),

    path("files", FileListAPIView.as_view(), name="files"),
    path("files/<int:pk>", FileRetrieveUpdateAPIView.as_view(), name="file"),
    path("create-file", FileCreateAPIView.as_view(), name="create-file"),
    path("change-status/<int:pk>", FileUpdateAPIView.as_view(), name="change-status"),
    path("delete-file/<int:pk>", FileDestroyAPIView.as_view(), name="delete-file"),
    
    path("get-file-logs", FileLogListAPIView.as_view(), name="get-file-logs")
]
