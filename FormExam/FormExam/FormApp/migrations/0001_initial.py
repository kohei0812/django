# Generated by Django 4.2.9 on 2024-05-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('picture', models.FileField(upload_to='student/')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
