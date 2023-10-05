# Generated by Django 4.1.2 on 2022-10-09 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_menu_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='cuisine',
            field=models.CharField(choices=[('0', 'None'), ('Ind', 'Indian'), ('Chn', 'Chinese'), ('Con', 'Continental'), ('Des', 'Desserts'), ('Sut', 'Sutta')], default='None', max_length=30),
        ),
    ]