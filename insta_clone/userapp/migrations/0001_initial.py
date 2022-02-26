# Generated by Django 4.0 on 2022-02-21 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('bio', models.CharField(blank=True, max_length=150)),
                ('profile_pic', models.FileField(blank=True, upload_to='profile_pic')),
                ('privete', models.BooleanField(default=False)),
                ('followers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='userapp.account')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='userapp.account')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
