# Generated by Django 3.2.4 on 2021-06-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_time', models.DateField(auto_now=True, null=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, null=True, verbose_name='是否删除')),
                ('username', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='账号')),
                ('nickname', models.CharField(max_length=30, null=True, verbose_name='昵称')),
                ('password', models.CharField(default='', max_length=128, verbose_name='密码')),
                ('salt', models.CharField(blank=True, default='', max_length=30, verbose_name='加密盐')),
                ('introduce', models.TextField(blank=True, null=True, verbose_name='个人简介')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload/avatar', verbose_name='头像')),
                ('sex', models.IntegerField(choices=[(1, '男'), (0, '女')], null=True, verbose_name='性别')),
            ],
            options={
                'verbose_name': '会员列表',
                'verbose_name_plural': '会员列表',
            },
        ),
    ]