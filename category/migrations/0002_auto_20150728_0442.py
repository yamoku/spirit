# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def default_categories(apps, schema_editor):
    Category = apps.get_model("spirit_category", "Category")

    if not Category.objects.filter(pk=settings.ST_TOPIC_PRIVATE_CATEGORY_PK).exists():
        Category.objects.create(
            pk=settings.ST_TOPIC_PRIVATE_CATEGORY_PK,
            title="Private",
            slug="private",
            is_private=True
        )

    if not Category.objects.filter(pk=settings.ST_UNCATEGORIZED_CATEGORY_PK).exists():
        Category.objects.create(
            pk=settings.ST_UNCATEGORIZED_CATEGORY_PK,
            title="Uncategorized",
            slug="uncategorized"
        )


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_category', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_categories),
    ]
