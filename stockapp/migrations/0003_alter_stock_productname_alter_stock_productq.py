# Generated by Django 4.1.7 on 2023-02-21 08:18

from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('stockapp', '0002_alter_stock_productname_alter_stock_productp_and_more'),
    ]
    operations = [
        migrations.AlterField(
            model_name='stock',
            name='productName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stock',
            name='productQ',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
