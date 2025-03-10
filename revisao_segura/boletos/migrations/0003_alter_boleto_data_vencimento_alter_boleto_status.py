# Generated by Django 5.1.6 on 2025-03-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletos', '0002_auto_20250309_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='data_vencimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='status',
            field=models.CharField(choices=[('pago', 'Pago'), ('pendente', 'Pendente'), ('vencido', 'Vencido')], default='pendente', max_length=10),
        ),
    ]
