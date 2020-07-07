# Generated by Django 3.0.5 on 2020-07-05 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Place')),
                ('noPassenger', models.IntegerField(blank=True, default=0, verbose_name='No. of Passengers')),
                ('total', models.IntegerField(blank=True, default=0, verbose_name='Total bill')),
                ('DOJ', models.DateField(blank=True, null=True, verbose_name='Date of journey')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
