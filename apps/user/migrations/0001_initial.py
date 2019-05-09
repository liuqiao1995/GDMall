# Generated by Django 2.0.6 on 2019-05-09 17:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('openid', models.CharField(max_length=50, verbose_name='用户openid')),
                ('nick_name', models.CharField(blank=True, max_length=50, verbose_name='昵称')),
                ('head_portrait', models.CharField(blank=True, max_length=255, verbose_name='用户头像')),
                ('birthday', models.CharField(blank=True, max_length=50, verbose_name='出生日期')),
                ('height', models.CharField(blank=True, default=0, max_length=30, verbose_name='身高')),
                ('weight', models.CharField(blank=True, default=0, max_length=30, verbose_name='体重')),
                ('phone', models.CharField(default=0, max_length=11, verbose_name='手机号码')),
                ('integral', models.IntegerField(default=0, verbose_name='会员积分')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'gd_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('addressee', models.CharField(max_length=30, verbose_name='收件人')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='联系人电话')),
                ('shipping_address', models.CharField(max_length=255, verbose_name='收件地址')),
                ('is_default', models.BooleanField(default=0, verbose_name='是否默认')),
                ('openid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户openid')),
            ],
            options={
                'verbose_name': '收货地址信息',
                'verbose_name_plural': '收货地址信息',
                'db_table': 'gd_address',
            },
        ),
        migrations.CreateModel(
            name='VipLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('level', models.CharField(max_length=20, verbose_name='等级名称')),
                ('minmum_integral', models.IntegerField(verbose_name='积分要求值')),
            ],
            options={
                'verbose_name': '会员等级',
                'verbose_name_plural': '会员等级',
                'db_table': 'gd_vip_level',
            },
        ),
    ]
