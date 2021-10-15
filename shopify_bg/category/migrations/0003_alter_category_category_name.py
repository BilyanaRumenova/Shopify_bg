# Generated by Django 3.2.8 on 2021-10-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('jackets', 'Jackets'), ('jeans', 'Jeans'), ('shirts', 'Shirts'), ('shoes', 'Shoes'), ('t-shirts', 'T-Shirts')], max_length=50, unique=True),
        ),
    ]
