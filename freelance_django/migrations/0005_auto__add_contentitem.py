# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContentItem'
        db.create_table(u'freelance_django_contentitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_landing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_blog', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'freelance_django', ['ContentItem'])


    def backwards(self, orm):
        # Deleting model 'ContentItem'
        db.delete_table(u'freelance_django_contentitem')


    models = {
        u'freelance_django.contentitem': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'ContentItem'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_landing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'freelance_django.portfolioitem': {
            'Meta': {'ordering': "('position',)", 'object_name': 'PortfolioItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'responsibilities': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['freelance_django.PortfolioTag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'freelance_django.portfoliotag': {
            'Meta': {'object_name': 'PortfolioTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['freelance_django']