# Generated by Django 3.2.12 on 2022-08-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20220804_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='photo',
            field=models.ImageField(default='default/error image.png', upload_to='about/'),
        ),
    ]