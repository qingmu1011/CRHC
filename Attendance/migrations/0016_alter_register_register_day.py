# Generated by Django 3.2.4 on 2021-06-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0015_register_register_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_day',
            field=models.IntegerField(default=1, verbose_name='请假天数'),
        ),
    ]
