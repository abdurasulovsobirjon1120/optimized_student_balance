# Generated by Django 5.1.4 on 2024-12-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_balance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(default="to'langan", max_length=20),
        ),
    ]
