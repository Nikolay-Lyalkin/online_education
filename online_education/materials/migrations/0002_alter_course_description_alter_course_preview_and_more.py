# Generated by Django 5.1.4 on 2024-12-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание курса"),
        ),
        migrations.AlterField(
            model_name="course",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="course image/"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание урока"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="link_on_video",
            field=models.URLField(blank=True, null=True, verbose_name="сылка на видео урока"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="lesson image/"),
        ),
    ]
