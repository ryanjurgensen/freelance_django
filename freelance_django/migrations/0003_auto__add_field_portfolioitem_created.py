# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PortfolioItem.created'
        db.add_column(u'freelance_django_portfolioitem', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 9, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PortfolioItem.created'
        db.delete_column(u'freelance_django_portfolioitem', 'created')


    models = {
        u'freelance_django.portfolioitem': {
            'Meta': {'ordering': "('position',)", 'object_name': 'PortfolioItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'responsibilities': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['freelance_django']