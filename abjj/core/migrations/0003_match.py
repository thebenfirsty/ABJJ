# Generated by Django 5.0.4 on 2025-03-08 21:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_bio_alter_profile_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_lost', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
