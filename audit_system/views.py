from rest_framework import generics
from rest_framework.response import Response

from functools import wraps

from .models import *
from .serializers import *


def log_to_system(log_msg):  # logging decorator
    def log_file(func):
        @wraps(func)
        def log(view, request, *args, **kwargs):

            # Get the user_id and file_id dynamically from the request and kwargs
            user = request.user
            file_id = kwargs.get(view.lookup_field)

            if file_id:
                file = File.objects.get(pk=file_id).title
            else:
                file = request.data.get("title")

            # Log to the FileLog model
            FileLog.objects.create(
                user_logged=user,
                file_logged=file,
                log_msg=log_msg
            )

            return func(view, request, *args, **kwargs)
        return log
    return log_file


class UserRegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.user

        if user.role == "manager":
            queryset = queryset.filter(role__in=["manager", "supervisor", "auditor"])

        if user.role == "supervisor":
            queryset = queryset.filter(role__in=["manager", "supervisor", "auditor"])

        if user.role == "auditor":
            queryset = queryset.filter(role__in=["supervisor", "auditor", "assistant"])

        if user.role == "assistant":
            queryset = queryset.filter(role__in=["auditor", "assistant"])

        return queryset


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        user_data = {
            'id': user.id,
            'username': user.username,
            'role': user.role
        }
        return Response(user_data)


class FileListAPIView(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        user = self.request.user

        if user.role == "manager":
            queryset = queryset.filter(assign_to__role__in=["manager", "supervisor", "auditor", "assistant"])

        if user.role == "supervisor":
            queryset = queryset.filter(assign_to__role__in=["manager", "supervisor", "auditor"])

        if user.role == "auditor":
            queryset = queryset.filter(assign_to__role__in=["supervisor", "auditor", "assistant"])

        if user.role == "assistant":
            queryset = queryset.filter(assign_to__role__in=["auditor", "assistant"])

        return queryset


class FileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @log_to_system(log_msg="updated file")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class FileCreateAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = CreateFileSerializer

    @log_to_system(log_msg="created file")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FileUpdateAPIView(generics.UpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileUpdateSerializer

    @log_to_system(log_msg="changed file status")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class FileDestroyAPIView(generics.DestroyAPIView):
    queryset = File.objects.all()

    @log_to_system(log_msg="deleted file")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FileLogListAPIView(generics.ListAPIView):
    queryset = FileLog.objects.all()
    serializer_class = FileLogSerializer
