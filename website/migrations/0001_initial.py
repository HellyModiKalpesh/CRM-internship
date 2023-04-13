# Generated by Django 4.2 on 2023-04-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(max_length=200)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
    ]
