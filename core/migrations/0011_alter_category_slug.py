# Generated by Django 4.1.5 on 2023-01-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_category_index_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
