# Generated by Django 3.2.13 on 2022-07-02 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220702_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='product.product'),
        ),
    ]
