# Generated by Django 4.1.5 on 2023-11-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestServicedesk', '0007_ticket_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='contact',
            field=models.CharField(default='Not provided', max_length=12),
        ),
    ]
