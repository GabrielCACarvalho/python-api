# Generated by Django 3.1.7 on 2021-04-10 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210409_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='promocao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.promocao'),
        ),
    ]
