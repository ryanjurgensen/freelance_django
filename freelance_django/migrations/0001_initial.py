# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PortfolioItem'
        db.create_table(u'freelance_django_portfolioitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('responsibilities', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'freelance_django', ['PortfolioItem'])


    def backwards(self, orm):
        # Deleting model 'PortfolioItem'
        db.delete_table(u'freelance_django_portfolioitem')


    models = {
        u'freelance_django.portfolioitem': {
            'Meta': {'object_name': 'PortfolioItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'responsibilities': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['freelance_django']