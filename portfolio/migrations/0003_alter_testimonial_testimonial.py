# Generated by Django 5.0 on 2025-01-20 20:45

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_experience_options_remove_experience_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Depoimento'),
        ),
    ]
