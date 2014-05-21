# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
        ('music', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('user_profile', models.ForeignKey(to='music.UserProfile', to_field='id')),
                ('track', models.ForeignKey(to='music.Track', to_field='id')),
                ('listen_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
