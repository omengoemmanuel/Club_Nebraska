# Generated by Django 3.2.24 on 2025-03-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neb', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='images/Events/default.jpg', upload_to='images/Events'),
        ),
    ]
