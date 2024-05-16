# Generated by Django 5.0.6 on 2024-05-16 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ej1', '0004_alter_cliente_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ej1.cliente'),
            preserve_default=False,
        ),
    ]