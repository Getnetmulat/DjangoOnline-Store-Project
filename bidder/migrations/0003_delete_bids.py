# Generated by Django 3.0.7 on 2023-06-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidder', '0002_bid_company_placement_placementbid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bids',
        ),
    ]
