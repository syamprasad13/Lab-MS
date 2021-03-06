# Generated by Django 2.2.6 on 2019-11-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msys', '0004_auto_20191125_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntryacl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('System_No', models.TextField()),
                ('Date', models.CharField(default='date', max_length=20)),
                ('Make', models.TextField(max_length=50)),
                ('Model_No', models.TextField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Particulars', models.TextField(max_length=100)),
                ('Remarks', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataEntrycc1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('System_No', models.TextField()),
                ('Date', models.CharField(default='date', max_length=20)),
                ('Make', models.TextField(max_length=50)),
                ('Model_No', models.TextField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Particulars', models.TextField(max_length=100)),
                ('Remarks', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataEntrycc2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('System_No', models.TextField()),
                ('Date', models.CharField(default='date', max_length=20)),
                ('Make', models.TextField(max_length=50)),
                ('Model_No', models.TextField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Particulars', models.TextField(max_length=100)),
                ('Remarks', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='DataEntry',
        ),
    ]
