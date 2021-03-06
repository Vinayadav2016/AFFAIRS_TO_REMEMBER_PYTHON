# Generated by Django 2.2.2 on 2019-07-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20190717_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='cusine1',
            field=models.CharField(choices=[('select_cusine', '--selectCusine--'), ('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('southindian', 'southindian'), ('italian', 'italian'), ('none', 'none')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine2',
            field=models.CharField(choices=[('select_cusine', '--selectCusine--'), ('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('southindian', 'southindian'), ('italian', 'italian'), ('none', 'none')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine3',
            field=models.CharField(choices=[('select_cusine', '--selectCusine--'), ('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('southindian', 'southindian'), ('italian', 'italian'), ('none', 'none')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine4',
            field=models.CharField(choices=[('select_cusine', '--selectCusine--'), ('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('southindian', 'southindian'), ('italian', 'italian'), ('none', 'none')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='drinks',
            field=models.CharField(choices=[('no', 'no'), ('select', '--select--'), ('yes', 'yes')], default='select1', help_text='enter yes or no', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='typef',
            field=models.CharField(choices=[('both', 'both'), ('select_type', '--selecttype--'), ('veg', 'veg'), ('non-veg', 'non-veg')], default='select_type', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='venuemodel',
            name='city',
            field=models.CharField(choices=[('select_city', '--selectcity--'), ('Udaipur', 'udaipar'), ('Jodhpur', 'jodhpur'), ('Mumbai', 'mumbai'), ('Jaipur', 'JAIPUR'), ('Banglore', 'banglore'), ('Delhi', 'delhi'), ('Nagpur', 'nagpur'), ('Chennai', 'chennai')], default='select_city', help_text='enter city', max_length=255),
        ),
    ]
