# Generated by Django 2.2.2 on 2019-07-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190716_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinner',
            name='cusine1',
            field=models.CharField(choices=[('none', 'none'), ('select_cusine', '--selectCusine--'), ('italian', 'italian'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('chinese', 'chinese')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine2',
            field=models.CharField(choices=[('none', 'none'), ('select_cusine', '--selectCusine--'), ('italian', 'italian'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('chinese', 'chinese')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine3',
            field=models.CharField(choices=[('none', 'none'), ('select_cusine', '--selectCusine--'), ('italian', 'italian'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('chinese', 'chinese')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine4',
            field=models.CharField(choices=[('none', 'none'), ('select_cusine', '--selectCusine--'), ('italian', 'italian'), ('northindian', 'northindian'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('chinese', 'chinese')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='drinks',
            field=models.CharField(choices=[('no', 'no'), ('select', '--select--'), ('yes', 'yes')], default='select1', help_text='enter yes or no', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='typef',
            field=models.CharField(choices=[('select_type', '--selecttype--'), ('veg', 'veg'), ('non-veg', 'non-veg'), ('both', 'both')], default='select_type', help_text='enter cusine', max_length=255),
        ),
    ]
