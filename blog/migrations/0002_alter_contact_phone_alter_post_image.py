# Generated by Django 5.0.4 on 2024-04-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=212),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
