# Generated by Django 4.0.3 on 2022-06-10 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='opdcomplainmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chiefcomplain', models.CharField(max_length=500)),
                ('pastcomplain', models.CharField(max_length=500)),
                ('followupvisit', models.CharField(max_length=500)),
                ('opdcomplain_UHID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='++', to='homepage.homepagemodel')),
            ],
        ),
    ]
