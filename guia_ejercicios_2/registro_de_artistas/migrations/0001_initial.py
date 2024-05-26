# Generated by Django 4.2 on 2024-05-25 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cantante', models.BooleanField(default=False)),
                ('instrumento', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ArtistaGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField()),
                ('creacion_registro', models.DateField()),
                ('agregado_por', models.CharField(max_length=50)),
                ('artista_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_de_artistas.artista')),
                ('grupo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registro_de_artistas.grupo')),
            ],
        ),
        migrations.AddField(
            model_name='artista',
            name='grupos',
            field=models.ManyToManyField(related_name='artistas', through='registro_de_artistas.ArtistaGrupo', to='registro_de_artistas.grupo'),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('grupo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albumes', to='registro_de_artistas.grupo')),
            ],
        ),
    ]