# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field friend_list on 'ChatUser'
        m2m_table_name = db.shorten_name(u'chat_chatuser_friend_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_chatuser', models.ForeignKey(orm[u'chat.chatuser'], null=False)),
            ('to_chatuser', models.ForeignKey(orm[u'chat.chatuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_chatuser_id', 'to_chatuser_id'])


    def backwards(self, orm):
        # Removing M2M table for field friend_list on 'ChatUser'
        db.delete_table(db.shorten_name(u'chat_chatuser_friend_list'))


    models = {
        u'chat.chatuser': {
            'Meta': {'object_name': 'ChatUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'avatars/noavatar.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'friend_list': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friend_list_rel_+'", 'to': u"orm['chat.ChatUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '10'})
        },
        u'chat.message': {
            'Meta': {'object_name': 'Message'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'null': 'True', 'to': u"orm['chat.ChatUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'null': 'True', 'to': u"orm['chat.ChatUser']"})
        }
    }

    complete_apps = ['chat']