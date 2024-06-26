# Generated by Django 4.1.13 on 2024-04-24 15:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='availableSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_slots', models.IntegerField()),
            ],
            options={
                'ordering': ('-available_slots',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='historytab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.CharField(max_length=255)),
                ('start', models.TimeField(auto_now_add=True)),
                ('end', models.TimeField(auto_now_add=True)),
                ('duration', models.TimeField(auto_now_add=True)),
                ('date_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_at',),
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-notification',),
            },
        ),
        migrations.CreateModel(
            name='parkingSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_slots', models.IntegerField()),
            ],
            options={
                'ordering': ('-parking_slots',),
            },
        ),
        migrations.CreateModel(
            name='real_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence', models.FloatField()),
                ('plate', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-plate',),
            },
        ),
        migrations.CreateModel(
            name='totalSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_slots', models.IntegerField()),
            ],
            options={
                'ordering': ('-total_slots',),
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.CharField(max_length=255)),
                ('announcement', models.TextField()),
                ('start', models.TimeField(auto_now_add=True)),
                ('end', models.TimeField()),
                ('duration', models.TimeField(max_length=255)),
                ('date_at', models.DateTimeField(auto_now_add=True)),
                ('Total_parking_Slots', models.IntegerField(default=50)),
                ('Vehicles_Parked', models.IntegerField(default=0)),
                ('Available_slots', models.IntegerField(default=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.category')),
            ],
            options={
                'ordering': ('-date_at',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', job.models.CustomUserManager()),
            ],
        ),
    ]
