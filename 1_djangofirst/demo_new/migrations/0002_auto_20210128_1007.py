# Generated by Django 2.2 on 2021-01-28 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_10', models.CharField(blank=True, max_length=10)),
                ('isbn_13', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo_new.BookNumber'),
        ),
    ]
