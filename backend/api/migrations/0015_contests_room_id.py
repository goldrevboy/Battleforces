# Generated by Django 5.1.1 on 2024-10-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_participants_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='room_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
