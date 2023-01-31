# Generated by Django 4.1.5 on 2023-01-30 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('name',), 'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.AlterIndexTogether(
            name='category',
            index_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='subcategory',
            index_together={('id', 'slug')},
        ),
    ]