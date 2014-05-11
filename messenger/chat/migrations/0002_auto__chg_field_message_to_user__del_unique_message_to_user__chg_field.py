# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Message', fields ['from_user']
        db.delete_unique(u'chat_message', ['from_user_id'])

        # Removing unique constraint on 'Message', fields ['to_user']
        db.delete_unique(u'chat_message', ['to_user_id'])


        # Changing field 'Message.to_user'
        db.alter_column(u'chat_message', 'to_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['chat.ChatUser']))

        # Changing field 'Message.from_user'
        db.alter_column(u'chat_message', 'from_user_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['chat.ChatUser']))

    def backwards(self, orm):

        # Changing field 'Message.to_user'
        db.alter_column(u'chat_message', 'to_user_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['chat.ChatUser']))
        # Adding unique constraint on 'Message', fields ['to_user']
        db.create_unique(u'chat_message', ['to_user_id'])


        # Changing field 'Message.from_user'
        db.alter_column(u'chat_message', 'from_user_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['chat.ChatUser']))
        # Adding unique constraint on 'Message', fields ['from_user']
        db.create_unique(u'chat_message', ['from_user_id'])


    models = {
        u'chat.chatuser': {
            'Meta': {'object_name': 'ChatUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'static/avatars/noavatar.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        },
        u'chat.userfriends': {
            'Meta': {'object_name': 'UserFriends'},
            'friend_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chat.ChatUser']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['chat']