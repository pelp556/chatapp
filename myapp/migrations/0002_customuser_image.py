# Generated by Django 4.1.3 on 2022-11-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='', upload_to='image/', verbose_name='画像'),
        ),
    ]
