# Generated by Django 2.2.2 on 2019-09-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20190717_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='cusine1',
            field=models.CharField(choices=[('none', 'none'), ('bakery', 'bakery'), ('chinese', 'chinese'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine2',
            field=models.CharField(choices=[('none', 'none'), ('bakery', 'bakery'), ('chinese', 'chinese'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine3',
            field=models.CharField(choices=[('none', 'none'), ('bakery', 'bakery'), ('chinese', 'chinese'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine4',
            field=models.CharField(choices=[('none', 'none'), ('bakery', 'bakery'), ('chinese', 'chinese'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='drinks',
            field=models.CharField(choices=[('yes', 'yes'), ('select', '--select--'), ('no', 'no')], default='select1', help_text='enter yes or no', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='typef',
            field=models.CharField(choices=[('non-veg', 'non-veg'), ('both', 'both'), ('select_type', '--selecttype--'), ('veg', 'veg')], default='select_type', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='venuemodel',
            name='city',
            field=models.CharField(choices=[('Delhi', 'delhi'), ('Chennai', 'chennai'), ('select_city', '--selectcity--'), ('Banglore', 'banglore'), ('Nagpur', 'nagpur'), ('Jodhpur', 'jodhpur'), ('Mumbai', 'mumbai'), ('Udaipur', 'udaipar'), ('Jaipur', 'JAIPUR')], default='select_city', help_text='enter city', max_length=255),
        ),
    ]
