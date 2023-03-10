# Generated by Django 4.0.3 on 2022-06-16 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='round_notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_note_number', models.CharField(max_length=500)),
                ('date_rn', models.DateField(max_length=500)),
                ('time_rn', models.CharField(max_length=500)),
                ('rmo_dr_name', models.TimeField(max_length=500)),
                ('dr_name', models.TimeField(max_length=500)),
                ('visit_type', models.CharField(max_length=500)),
                ('symptoms', models.CharField(max_length=500)),
                ('examination', models.CharField(max_length=500)),
                ('nursing_advice', models.CharField(max_length=500)),
                ('lab_test_order', models.CharField(max_length=500)),
                ('diagnostic_test_order', models.CharField(max_length=500)),
                ('assessment', models.CharField(max_length=500)),
                ('treatement_plan', models.CharField(max_length=500)),
                ('blood_transfusion', models.CharField(max_length=500)),
                ('UHID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='++', to='homepage.homepagemodel')),
            ],
        ),
    ]
