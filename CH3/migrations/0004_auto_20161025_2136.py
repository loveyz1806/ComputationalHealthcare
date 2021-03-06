# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-25 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CH3', '0003_auto_20161025_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='N1Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_code', models.CharField(max_length=50)),
                ('initial', models.CharField(max_length=50)),
                ('sub', models.CharField(max_length=50)),
                ('dx', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('delta_median', models.IntegerField(default=-1)),
                ('filename', models.CharField(max_length=200)),
                ('pediatric', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='N2Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_code', models.CharField(max_length=50)),
                ('initial', models.CharField(max_length=50)),
                ('sub', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('key', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=200)),
                ('entry_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='N3Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_code', models.CharField(max_length=50)),
                ('initial', models.CharField(max_length=50)),
                ('sub', models.CharField(max_length=50)),
                ('count', models.IntegerField(default=0)),
                ('key', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=200)),
                ('entry_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='linked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='n3entry',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CH3.Dataset'),
        ),
        migrations.AddField(
            model_name='n2entry',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CH3.Dataset'),
        ),
        migrations.AddField(
            model_name='n1entry',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CH3.Dataset'),
        ),
    ]
