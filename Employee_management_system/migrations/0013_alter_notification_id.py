# Generated by Django 5.0.4 on 2024-05-13 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management_system', '0012_customuser_remaining_leave_leaverequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
