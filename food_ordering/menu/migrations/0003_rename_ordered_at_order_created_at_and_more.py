# Generated by Django 5.0.3 on 2024-05-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_rename_created_at_order_ordered_at_order_quantity_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="ordered_at",
            new_name="created_at",
        ),
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="order",
            name="user",
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
