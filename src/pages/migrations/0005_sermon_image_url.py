# Generated by Django 3.2.14 on 2023-03-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20230327_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermon',
            name='image_url',
            field=models.CharField(blank=True, default='sermons/default.jpg', max_length=200, null=True),
        ),
    ]