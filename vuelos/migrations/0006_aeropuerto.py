# Generated by Django 3.1.2 on 2020-10-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0005_remove_ciudad_ejemplo2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vuelos.ciudad')),
            ],
        ),
    ]
