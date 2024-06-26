# Generated by Django 3.2.16 on 2024-04-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_subscription_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='field_a',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='field_b',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['field_a', 'field_b'], name='services_su_field_a_155836_idx'),
        ),
    ]
