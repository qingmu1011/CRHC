# Generated by Django 3.2.4 on 2021-06-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0004_datascreen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auxiliary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auxiliary_sign', models.CharField(max_length=10)),
                ('auxiliary_type', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '标记类型',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_name', models.CharField(max_length=10)),
                ('leave_date', models.DateField()),
                ('leave_time_interval', models.CharField(choices=[('上午', '上午'), ('中午', '中午'), ('下午', '下午'), ('全天', '全天')], max_length=10)),
            ],
            options={
                'verbose_name_plural': '请假、外出、报备',
            },
        ),
    ]