# Generated by Django 5.0.6 on 2024-07-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election_System', '0007_rename_fn_completedvote_fullname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('partynm', models.CharField(max_length=50)),
                ('partyimg', models.ImageField(upload_to='images/')),
                ('vote', models.IntegerField(default=0)),
            ],
        ),
    ]
