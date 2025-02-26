# Generated by Django 5.0 on 2025-01-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['order'], 'verbose_name': 'Software/Recurso', 'verbose_name_plural': 'Softwares/Recursos'},
        ),
        migrations.RemoveField(
            model_name='experience',
            name='company',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='proficiency',
        ),
        migrations.AddField(
            model_name='experience',
            name='proficiency_level',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nível de Proficiência'),
        ),
        migrations.AddField(
            model_name='experience',
            name='version',
            field=models.CharField(blank=True, max_length=50, verbose_name='Versão'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='experience_type',
            field=models.CharField(blank=True, choices=[('design', 'Design'), ('development', 'Desenvolvimento'), ('tools', 'Ferramentas')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Nome do Software/Recurso'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(blank=True, max_length=50, verbose_name='Ícone FontAwesome'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(blank=True, choices=[('design', 'Design'), ('development', 'Desenvolvimento'), ('tools', 'Ferramentas')], max_length=20, verbose_name='Tipo'),
        ),
    ]
