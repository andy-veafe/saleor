# Generated by Django 3.2.6 on 2021-12-06 18:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0117_merge_20210903_1013"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="price_expiration_for_unconfirmed",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
