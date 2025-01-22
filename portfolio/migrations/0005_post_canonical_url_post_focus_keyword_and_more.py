# Generated by Django 5.0 on 2025-01-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_hero_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='canonical_url',
            field=models.URLField(blank=True, help_text='URL canônica se diferente da URL padrão', verbose_name='URL Canônica'),
        ),
        migrations.AddField(
            model_name='post',
            name='focus_keyword',
            field=models.CharField(blank=True, help_text='Palavra-chave principal para otimização', max_length=100, verbose_name='Palavra-chave Principal'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Descrição otimizada para SEO (máx. 160 caracteres)', max_length=160, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_keywords',
            field=models.CharField(blank=True, help_text='Palavras-chave separadas por vírgula', max_length=200, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title',
            field=models.CharField(blank=True, help_text='Título otimizado para SEO (máx. 60 caracteres)', max_length=60, verbose_name='Meta Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='og_description',
            field=models.TextField(blank=True, help_text='Descrição para compartilhamento em redes sociais', max_length=200, verbose_name='OG Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='og_image',
            field=models.ImageField(blank=True, help_text='Imagem para compartilhamento (1200x630px)', null=True, upload_to='blog/og', verbose_name='OG Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='og_title',
            field=models.CharField(blank=True, help_text='Título para compartilhamento em redes sociais', max_length=60, verbose_name='OG Title'),
        ),
    ]
