# Generated by Django 5.1.2 on 2024-10-15 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_geeros'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Geeros',
            new_name='Generos',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='fk_generos',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.generos'),
        ),
    ]
