# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Coupon'
        db.create_table('coupons_coupon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('promotion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coupons.Promotion'])),
            ('used', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('prize', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coupons.Prize'], null=True, blank=True)),
            ('redeemer_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('redeemer_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('redeemer_phone', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('redeemer_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('redeemer_city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('redeemer_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('redeemer_zip', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coupons', ['Coupon'])

        # Adding model 'Promotion'
        db.create_table('coupons_promotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('coupons', ['Promotion'])

        # Adding M2M table for field prizes on 'Promotion'
        db.create_table('coupons_promotion_prizes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotion', models.ForeignKey(orm['coupons.promotion'], null=False)),
            ('prize', models.ForeignKey(orm['coupons.prize'], null=False))
        ))
        db.create_unique('coupons_promotion_prizes', ['promotion_id', 'prize_id'])

        # Adding model 'Prize'
        db.create_table('coupons_prize', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('coupons', ['Prize'])


    def backwards(self, orm):
        
        # Deleting model 'Coupon'
        db.delete_table('coupons_coupon')

        # Deleting model 'Promotion'
        db.delete_table('coupons_promotion')

        # Removing M2M table for field prizes on 'Promotion'
        db.delete_table('coupons_promotion_prizes')

        # Deleting model 'Prize'
        db.delete_table('coupons_prize')


    models = {
        'coupons.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coupons.Prize']", 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coupons.Promotion']"}),
            'redeemer_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'redeemer_city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'redeemer_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'redeemer_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redeemer_phone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'redeemer_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'redeemer_zip': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'used': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'coupons.prize': {
            'Meta': {'object_name': 'Prize'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'coupons.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'prizes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coupons.Prize']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['coupons']
