# Generated by Django 5.1 on 2024-09-15 11:13

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusyTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_day', models.BooleanField(default=True)),
                ('for_boy', models.BooleanField(default=True)),
                ('rate', models.DecimalField(decimal_places=2, default=50.0, max_digits=5)),
                ('noPeople', models.PositiveIntegerField(default=1)),
                ('adminOp', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(choices=[('sobhaneh', 'Sobhaneh'), ('nahar', 'Nahar'), ('sham', 'Sham')], max_length=16)),
                ('date', models.DateField()),
                ('foodname', models.CharField(max_length=128)),
                ('awli_vote', models.PositiveIntegerField(default=0)),
                ('khob_vote', models.PositiveIntegerField(default=0)),
                ('bad_vote', models.PositiveIntegerField(default=0)),
                ('eftezah_vote', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_boy', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('noLogin', models.PositiveIntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='food.food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='food.menu'),
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.FloatField(default=0.0)),
                ('busy_tracking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='food.busytracking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together={('date', 'foodname')},
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(choices=[('awli', 'Awli'), ('khob', 'Khob'), ('bad', 'Bad'), ('eftezah', 'Eftezah')], max_length=8)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='food.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'food')},
            },
        ),
    ]
