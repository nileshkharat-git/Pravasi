# Generated by Django 3.0.5 on 2020-07-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='Email')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('Place', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=100)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='destination')),
                ('Description', models.TextField(max_length=150)),
                ('RateOfTicket', models.FloatField(null=True, verbose_name='Ticket rate')),
                ('inOffer', models.BooleanField(null=True, verbose_name='Offer')),
            ],
        ),
    ]