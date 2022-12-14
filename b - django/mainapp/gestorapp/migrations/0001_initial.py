# Generated by Django 4.1.2 on 2022-10-31 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('noExterior', models.CharField(max_length=255)),
                ('colonia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.CharField(max_length=255)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.alumno')),
                ('maestro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.maestro')),
            ],
        ),
        migrations.AddField(
            model_name='maestro',
            name='materia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.materia'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='materia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.materia'),
        ),
    ]
