from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('supervisor', 'supervisor'),
        ('auditor', 'auditor'),
        ('assistant', 'assistant'),
    )

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username

    def __str__(self):
        return f"{self.username} - {self.role}"


class File(models.Model):

    File_Type = (
        ('EXCEL', 'Excel'),
        ('PDF', 'PDF'),
        ('WORD', 'Word'),
        ('TXT', 'Text'),
        ('CSV', 'CSV'),
    )

    File_States = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved'),
    )

    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True)
    file = models.URLField(default='', blank=True, null=True)
    type = models.CharField(max_length=10, choices=File_Type)

    assign_to = models.ForeignKey(User, related_name='files', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=File_States, default='Pending')
    notes = models.TextField(blank=True, null=True)

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FileLog(models.Model):
    user_logged = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    file_logged = models.CharField(max_length=255, blank=True)
    log_msg = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.log_msg
