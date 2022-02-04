# Generated by Django 4.0.1 on 2022-01-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ContryOfTheUser', to='base.country'),
        ),
    ]