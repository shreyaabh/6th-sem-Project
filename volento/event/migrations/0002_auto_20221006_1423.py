# Generated by Django 3.2.9 on 2022-10-06 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsers',
            field=models.ManyToManyField(to='event.EventSponser'),
        ),
    ]