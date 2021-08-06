# Generated by Django 2.2.2 on 2019-07-16 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='enter phone no', max_length=255)),
                ('hname', models.CharField(help_text='resturant name', max_length=255)),
                ('date', models.DateTimeField(help_text='enter date')),
                ('person', models.CharField(help_text='no of persons', max_length=255)),
            ],
            options={
                'verbose_name': 'booking',
                'verbose_name_plural': 'bookings',
                'db_table': 'booking',
                'ordering': ('hname',),
            },
        ),
        migrations.CreateModel(
            name='dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(help_text='resturant name', max_length=255)),
                ('hadd', models.CharField(help_text='address of resturant', max_length=255)),
                ('hpp', models.CharField(help_text='price per person', max_length=255)),
                ('himage1', models.ImageField(blank=True, upload_to='hreg')),
                ('himage2', models.ImageField(blank=True, upload_to='hreg')),
                ('cusine1', models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian'), ('bakery', 'bakery'), ('southindian', 'southindian')], default='select_cusine', help_text='enter cusine', max_length=255)),
                ('cusine2', models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian'), ('bakery', 'bakery'), ('southindian', 'southindian')], default='select_cusine', help_text='enter cusine', max_length=255)),
                ('cusine3', models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian'), ('bakery', 'bakery'), ('southindian', 'southindian')], default='select_cusine', help_text='enter cusine', max_length=255)),
                ('cusine4', models.CharField(choices=[('northindian', 'northindian'), ('chinese', 'chinese'), ('fastfood', 'fastfood'), ('select_cusine', '--selectCusine--'), ('none', 'none'), ('italian', 'italian'), ('bakery', 'bakery'), ('southindian', 'southindian')], default='select_cusine', help_text='enter cusine', max_length=255)),
                ('drinks', models.CharField(choices=[('No', 'no'), ('select', '--select--'), ('Yes', 'yes')], default='select1', help_text='enter yes or no', max_length=255)),
                ('typef', models.CharField(choices=[('both', 'both'), ('non-veg', 'non-veg'), ('veg', 'veg'), ('select_type', '--selecttype--')], default='select_type', help_text='enter cusine', max_length=255)),
            ],
            options={
                'verbose_name': 'hreg',
                'verbose_name_plural': 'hregs',
                'db_table': 'hreg',
                'ordering': ('hpp',),
            },
        ),
        migrations.CreateModel(
            name='usercom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(help_text='resturant name', max_length=255)),
                ('pname', models.CharField(help_text='person name', max_length=255)),
                ('comments', models.CharField(help_text='comments', max_length=255)),
            ],
            options={
                'verbose_name': 'comments',
                'verbose_name_plural': 'commentss',
                'db_table': 'comments',
                'ordering': ('pname',),
            },
        ),
    ]