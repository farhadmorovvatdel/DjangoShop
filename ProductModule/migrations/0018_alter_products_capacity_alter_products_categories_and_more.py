# Generated by Django 4.2.1 on 2023-08-06 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductModule', '0017_alter_products_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='capacity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductCapacity', related_query_name='prcapcity', to='ProductModule.capacity'),
        ),
        migrations.AlterField(
            model_name='products',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductCategory', related_query_name='prcat', to='ProductModule.categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductColor', related_query_name='prcolor', to='ProductModule.colors'),
        ),
    ]
