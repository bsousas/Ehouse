# Generated by Django 2.1.1 on 2018-10-10 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20181010_0215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imovel',
            options={'ordering': ['cidade'], 'verbose_name': 'imovel', 'verbose_name_plural': 'imoveis'},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Título do anúncio'),
        ),
    ]