# Generated by Django 4.0 on 2022-02-21 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='privete',
            new_name='private',
        ),
        migrations.AlterField(
            model_name='account',
            name='followers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='userapp.account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='following',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_following', to='userapp.account'),
        ),
    ]