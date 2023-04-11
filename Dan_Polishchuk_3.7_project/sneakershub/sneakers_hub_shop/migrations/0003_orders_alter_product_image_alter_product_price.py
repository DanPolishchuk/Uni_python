# Generated by Django 4.1.7 on 2023-04-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers_hub_shop', '0002_product_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model', models.CharField(max_length=255)),
                ('Price', models.CharField(max_length=255)),
                ('Size', models.CharField(max_length=255)),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]