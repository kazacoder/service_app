# Generated by Django 3.2.16 on 2024-04-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='comment',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
