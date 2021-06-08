# Generated by Django 3.1.7 on 2021-03-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=5, verbose_name='Matricule')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom')),
            ],
        ),
    ]