# Generated by Django 4.2 on 2023-05-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_team_leader_remove_team_members_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='role',
            field=models.CharField(default='MEMBER', max_length=10),
        ),
        migrations.AlterField(
            model_name='participant',
            name='status',
            field=models.CharField(default='PENDING', max_length=100),
        ),
    ]
