# Generated by Django 4.2.4 on 2023-08-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='qty',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]