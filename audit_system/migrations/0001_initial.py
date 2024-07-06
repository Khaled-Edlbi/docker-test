# Generated by Django 4.2.5 on 2024-06-18 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('supervisor', 'Supervisor'), ('auditor', 'Auditor'), ('assistant', 'Assistant')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.URLField(blank=True, default='', null=True)),
                ('type', models.CharField(choices=[('EXCEL', 'Excel'), ('PDF', 'PDF'), ('WORD', 'Word'), ('TXT', 'Text'), ('CSV', 'CSV')], max_length=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('assign_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]