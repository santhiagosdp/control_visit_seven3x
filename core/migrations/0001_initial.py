# Generated by Django 3.2.11 on 2023-01-31 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('fone', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=150)),
                ('complemento', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True)),
                ('descricao', models.TextField(max_length=5000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.visitante')),
            ],
        ),
    ]
