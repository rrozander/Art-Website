# Generated by Django 3.2.12 on 2022-03-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_about_description'),
        ('art', '0005_remove_art_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Art',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='artimage',
            old_name='art_project',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='artimage',
            name='image',
            field=models.ImageField(upload_to='art_images/'),
        ),
    ]
