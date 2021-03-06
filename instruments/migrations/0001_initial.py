# Generated by Django 3.1.7 on 2021-04-04 08:48

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContamStatus',
            fields=[
                ('contam_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('contam_status', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'contam_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=64, null=True)),
                ('site_name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('instrument_type_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('instrument_types', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'instrument_uses',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('instrument_location', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'instrument_location',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('instrument_status', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'instrument_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InstrumentModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=48)),
                ('model', models.CharField(max_length=48)),
                ('instrument_type', models.ForeignKey(blank=True, db_column='instrument_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.instrumenttype')),
            ],
            options={
                'db_table': 'instrument_models',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('instrument_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=24)),
                ('cal_due', models.DateField(db_column='cal_due')),
                ('notes', models.CharField(blank=True, db_column='notes', max_length=512, null=True)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, max_length=200, null=True, populate_from='serial_number', unique=True)),
                ('contam_status', models.ForeignKey(blank=True, db_column='contam_status', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.contamstatus')),
                ('instrument_model', models.ForeignKey(blank=True, db_column='instrument_model', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.instrumentmodels')),
                ('location', models.ForeignKey(blank=True, db_column='location', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.location')),
                ('owner', models.ForeignKey(blank=True, db_column='owner', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.customer')),
                ('status', models.ForeignKey(blank=True, db_column='status', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='instruments.status')),
            ],
            options={
                'db_table': 'instruments',
                'managed': True,
            },
        ),
    ]
