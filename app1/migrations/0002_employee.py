# Generated by Django 4.2.10 on 2024-03-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50, null=True)),
                ('emp_email', models.EmailField(max_length=70, null=True)),
                ('emp_phone', models.IntegerField(null=True)),
            ],
        ),
    ]
