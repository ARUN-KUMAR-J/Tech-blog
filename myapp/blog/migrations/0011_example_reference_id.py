# Generated by Django 4.2.13 on 2024-07-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='example',
            name='reference_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
