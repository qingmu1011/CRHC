# Generated by Django 3.2.4 on 2021-06-25 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0007_auto_20210625_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datascreen',
            name='check_explain',
        ),
    ]
