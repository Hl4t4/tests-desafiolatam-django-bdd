# Generated by Django 4.2 on 2024-05-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='ciudad',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]