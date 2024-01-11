# Generated by Django 5.0.1 on 2024-01-10 19:31

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classificados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banner_classificados')),
            ],
        ),
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituto', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='imagens_destaques')),
                ('texto', ckeditor_uploader.fields.RichTextUploadingField()),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens_eventos')),
            ],
        ),
        migrations.CreateModel(
            name='Programacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituto', models.CharField(max_length=200)),
                ('resumo', models.CharField(max_length=250)),
                ('imagem', models.ImageField(upload_to='imagens_publicacoes')),
                ('texto', ckeditor_uploader.fields.RichTextUploadingField()),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
    ]
