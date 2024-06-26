# Generated by Django 4.2 on 2024-05-25 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('patente', models.CharField(max_length=6, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('conductor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_conductores.conductor')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(max_length=10)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('conductor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro_conductores.conductor')),
            ],
        ),
    ]
