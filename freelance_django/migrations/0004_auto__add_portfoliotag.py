# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PortfolioTag'
        db.create_table(u'freelance_django_portfoliotag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'freelance_django', ['PortfolioTag'])

        # Adding M2M table for field tags on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'freelance_django_portfolioitem_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'freelance_django.portfolioitem'], null=False)),
            ('portfoliotag', models.ForeignKey(orm[u'freelance_django.portfoliotag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfoliotag_id'])


    def backwards(self, orm):
        # Deleting model 'PortfolioTag'
        db.delete_table(u'freelance_django_portfoliotag')

        # Removing M2M table for field tags on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'freelance_django_portfolioitem_tags'))


    models = {
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