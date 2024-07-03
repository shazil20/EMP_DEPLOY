# Generated by Django 5.0.4 on 2024-05-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management_system', '0007_remove_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=50, null=True),
        ),
    ]
