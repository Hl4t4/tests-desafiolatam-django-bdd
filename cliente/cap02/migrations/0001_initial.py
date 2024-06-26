# Generated by Django 5.0.6 on 2024-05-25 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(max_length=10, null=True)),
                ('comuna', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=10)),
                ('cliente_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cap02.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='AutorLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_por', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cap02.autor')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cap02.libro')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='libros',
            field=models.ManyToManyField(related_name='autores', through='cap02.AutorLibro', to='cap02.libro'),
        ),
    ]
