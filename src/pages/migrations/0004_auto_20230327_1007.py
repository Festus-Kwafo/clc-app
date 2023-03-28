# Generated by Django 3.2.14 on 2023-03-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20230327_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sermon',
            name='image',
        ),
        migrations.AddField(
            model_name='sermon',
            name='image_desktop',
            field=models.ImageField(default='sermons/default.jpg', upload_to='sermons/'),
        ),
        migrations.AddField(
            model_name='sermon',
            name='image_mobile',
            field=models.ImageField(default='sermons/default.jpg', upload_to='sermons/'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='audio',
            field=models.FileField(upload_to='sermons/'),
        ),
    ]
