# Generated by Django 5.0.7 on 2024-07-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='local_images/default.jpg', upload_to='local_images/'),
        ),
    ]
