# Generated by Django 2.2.2 on 2019-07-16 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20190717_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='cusine1',
            field=models.CharField(choices=[('southindian', 'southindian'), ('chinese', 'chinese'), ('none', 'none'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('northindian', 'northindian'), ('italian', 'italian'), ('select_cusine', '--selectCusine--')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine2',
            field=models.CharField(choices=[('southindian', 'southindian'), ('chinese', 'chinese'), ('none', 'none'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('northindian', 'northindian'), ('italian', 'italian'), ('select_cusine', '--selectCusine--')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine3',
            field=models.CharField(choices=[('southindian', 'southindian'), ('none', 'none'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('northindian', 'northindian'), ('italian', 'italian'), ('select_cusine', '--selectCusine--')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine4',
            field=models.CharField(choices=[('southindian', 'southindian'), ('chinese', 'chinese'), ('none', 'none'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('northindian', 'northindian'), ('italian', 'italian'), ('select_cusine', '--selectCusine--')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='drinks',
            field=models.CharField(choices=[('select', '--select--'), ('yes', 'yes'), ('no', 'no')], default='select1', help_text='enter yes or no', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='typef',
            field=models.CharField(choices=[('select_type', '--selecttype--'), ('veg', 'veg'), ('both', 'both'), ('non-veg', 'non-veg')], default='select_type', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='venuemodel',
            name='city',
            field=models.CharField(choices=[('Udaipur', 'udaipar'), ('Jodhpur', 'jodhpur'), ('Chennai', 'chennai'), ('Mumbai', 'mumbai'), ('Delhi', 'delhi'), ('Nagpur', 'nagpur'), ('Jaipur', 'JAIPUR'), ('select_city', '--selectcity--'), ('Banglore', 'banglore')], default='select_city', help_text='enter city', max_length=255),
        ),
    ]
