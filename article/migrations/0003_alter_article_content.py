# Generated by Django 4.2.1 on 2023-07-12 08:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_article_article_image_alter_article_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor.fields.RichTextField(verbose_name="İçerik"),
        ),
    ]
