# Generated by Django 4.0.3 on 2022-06-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_alter_offer_finalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='endingbet',
            field=models.DateTimeField(),
        ),
    ]
