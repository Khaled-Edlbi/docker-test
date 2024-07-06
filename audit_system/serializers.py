from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']


class FileSerializer(serializers.ModelSerializer):
    assign_to = UserSerializer(read_only=True)

    class Meta:
        model = File
        fields = '__all__'


class CreateFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'title',
            'description',
            'file',
            'type',
            'assign_to',
        ]


class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['assign_to', 'status', 'notes']


class FileLogSerializer(serializers.ModelSerializer):
    user_logged = UserSerializer(read_only=True)

    class Meta:
        model = FileLog
        fields = "__all__"
