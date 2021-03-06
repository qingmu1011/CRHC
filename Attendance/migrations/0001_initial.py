# Generated by Django 3.2.4 on 2021-06-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_num', models.CharField(max_length=40, verbose_name='编号')),
                ('user_date', models.DateField(verbose_name='打卡日期')),
                ('user_time', models.TimeField(verbose_name='打卡时间')),
            ],
            options={
                'verbose_name': '打卡记录',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_num', models.CharField(max_length=40, verbose_name='编号')),
                ('user_name', models.CharField(max_length=40, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '人员',
            },
        ),
    ]
