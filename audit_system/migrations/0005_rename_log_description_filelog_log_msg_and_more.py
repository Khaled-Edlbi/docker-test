# Generated by Django 4.2.5 on 2024-06-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit_system', '0004_remove_filelog_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filelog',
            old_name='log_description',
            new_name='log_msg',
        ),
        migrations.AlterField(
            model_name='filelog',
            name='file_logged',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
