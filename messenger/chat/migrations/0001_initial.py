# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChatUser'
        db.create_table(u'chat_chatuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=10)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(default='media/avatars/noavatar.png', max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'chat', ['ChatUser'])

        # Adding model 'UserFriends'
        db.create_table(u'chat_userfriends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'chat', ['UserFriends'])

        # Adding M2M table for field friend_list on 'UserFriends'
        m2m_table_name = db.shorten_name(u'chat_userfriends_friend_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userfriends', models.ForeignKey(orm[u'chat.userfriends'], null=False)),
            ('chatuser', models.ForeignKey(orm[u'chat.chatuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userfriends_id', 'chatuser_id'])

        # Adding model 'Message'
        db.create_table(u'chat_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', null=True, to=orm['chat.ChatUser'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', null=True, to=orm['chat.ChatUser'])),
            ('is_read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'chat', ['Message'])


    def backwards(self, orm):
        # Deleting model 'ChatUser'
        db.delete_table(u'chat_chatuser')

        # Deleting model 'UserFriends'
        db.delete_table(u'chat_userfriends')

        # Removing M2M table for field friend_list on 'UserFriends'
        db.delete_table(db.shorten_name(u'chat_userfriends_friend_list'))

        # Deleting model 'Message'
        db.delete_table(u'chat_message')


    models = {
        u'chat.chatuser': {
            'Meta': {'object_name': 'ChatUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'media/avatars/noavatar.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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