# Generated by Django 2.2.2 on 2019-07-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190716_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='venuemodel',
            name='image3',
            field=models.ImageField(blank=True, upload_to='venue'),
        ),
        migrations.AddField(
            model_name='venuemodel',
            name='image4',
            field=models.ImageField(blank=True, upload_to='venue'),
        ),
        migrations.AddField(
            model_name='venuemodel',
            name='image5',
            field=models.ImageField(blank=True, upload_to='venue'),
        ),
        migrations.AddField(
            model_name='venuemodel',
            name='image6',
            field=models.ImageField(blank=True, upload_to='venue'),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine1',
            field=models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine2',
            field=models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine3',
            field=models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='cusine4',
            field=models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('southindian', 'southindian'), ('fastfood', 'fastfood'), ('bakery', 'bakery'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian')], default='select_cusine', help_text='enter cusine', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='drinks',
            field=models.CharField(choices=[('select', '--select--'), ('no', 'no'), ('yes', 'yes')], default='select1', help_text='enter yes or no', max_length=255),
        ),
        migrations.AlterField(
            model_name='dinner',
            name='typef',
            field=models.CharField(choices=[('both', 'both'), ('veg', 'veg'), ('select_type', '--selecttype--'), ('non-veg', 'non-veg')], default='select_type', help_text='enter cusine', max_length=255),
        ),
    ]