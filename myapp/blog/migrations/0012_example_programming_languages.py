# Generated by Django 4.2.13 on 2024-07-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_example_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='Programming_Languages',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
