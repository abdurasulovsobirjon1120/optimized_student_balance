# Generated by Django 5.1.4 on 2024-12-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_balance', '0003_alter_student_first_name_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
            ],
        ),
    ]