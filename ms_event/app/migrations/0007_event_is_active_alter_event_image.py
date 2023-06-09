# Generated by Django 4.2 on 2023-04-22 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_event_author_remove_event_tags_delete_eventtag_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/events/"),
        ),
    ]
