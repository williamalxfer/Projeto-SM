# Generated by Django 2.2.1 on 2019-09-03 23:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('assunto', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('marca', models.CharField(default='', max_length=100)),
                ('descricao', models.TextField()),
                ('unidade', models.CharField(choices=[('UN', 'UN'), ('PC', 'PC'), ('KG', 'KG'), ('LT', 'LT'), ('PÇ', 'PÇ')], max_length=2)),
                ('valor', models.FloatField(default=0.0)),
                ('quantidade', models.IntegerField(default=0)),
                ('foto', models.FileField(blank=True, upload_to='%Y/%m/%d/')),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('curtidas', models.IntegerField(default=0)),
                ('descurtidas', models.IntegerField(default=0)),
                ('visualizacoes', models.IntegerField(default=0)),
            ],
        ),
    ]