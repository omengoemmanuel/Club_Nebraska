# Generated by Django 3.2.24 on 2025-03-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neb', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poa', models.CharField(max_length=100)),
                ('X_link', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
