# Generated by Django 3.2.4 on 2021-06-26 09:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('short_description', models.TextField(default='', max_length=250)),
                ('description', ckeditor.fields.RichTextField(default='', max_length=5000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=150, null=True)),
                ('blog_thumbnil', models.FileField(blank=True, null=True, upload_to='blog')),
                ('blog_main_pic', models.FileField(blank=True, null=True, upload_to='blog')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
