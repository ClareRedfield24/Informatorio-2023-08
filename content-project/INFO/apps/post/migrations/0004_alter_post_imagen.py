# Generated by Django 4.2.2 on 2023-08-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='static/post_default.png', upload_to='media'),
        ),
    ]
