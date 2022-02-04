# Generated by Django 4.0.1 on 2022-02-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=194, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=194, unique=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Dev',
                'verbose_name_plural': 'Devs',
                'ordering': ['email'],
            },
        ),
    ]