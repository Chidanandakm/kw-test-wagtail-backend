# Generated by Django 4.2.5 on 2023-09-19 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("blog", "0005_blogpagetag_blogpage_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpagegalleryimage",
            name="image",
        ),
        migrations.RemoveField(
            model_name="blogpagegalleryimage",
            name="page",
        ),
        migrations.RemoveField(
            model_name="blogpagetag",
            name="content_object",
        ),
        migrations.RemoveField(
            model_name="blogpagetag",
            name="tag",
        ),
        migrations.RemoveField(
            model_name="blogpage",
            name="authors",
        ),
        migrations.RemoveField(
            model_name="blogpage",
            name="intro",
        ),
        migrations.RemoveField(
            model_name="blogpage",
            name="tags",
        ),
        migrations.AddField(
            model_name="blogpage",
            name="author",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="blogpage",
            name="image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.DeleteModel(
            name="Author",
        ),
        migrations.DeleteModel(
            name="BlogPageGalleryImage",
        ),
        migrations.DeleteModel(
            name="BlogPageTag",
        ),
    ]
