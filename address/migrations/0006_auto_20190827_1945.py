# Generated by Django 2.2 on 2019-08-28 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_address_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locality',
            options={'ordering': ('name',), 'verbose_name_plural': 'Localities'},
        ),
        migrations.AlterModelOptions(
            name='neighborhood',
            options={'ordering': ('name',), 'verbose_name_plural': 'Neighborhoods'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ('name',)},
        ),
    ]
