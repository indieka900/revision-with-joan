# Generated by Django 4.2.6 on 2023-11-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(default='profile.png', upload_to='students'),
        ),
    ]