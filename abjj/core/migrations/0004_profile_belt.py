# Generated by Django 5.0.4 on 2025-03-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='belt',
            field=models.CharField(choices=[('White', 'White'), ('Blue', 'Blue'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Black', 'Black')], default='white', max_length=6),
        ),
    ]
