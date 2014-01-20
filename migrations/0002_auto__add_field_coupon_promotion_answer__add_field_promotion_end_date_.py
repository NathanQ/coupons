# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Coupon.promotion_answer'
        db.add_column('coupons_coupon', 'promotion_answer', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Promotion.end_date'
        db.add_column('coupons_promotion', 'end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Promotion.video_embed_code'
        db.add_column('coupons_promotion', 'video_embed_code', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Promotion.promotion_question'
        db.add_column('coupons_promotion', 'promotion_question', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Coupon.promotion_answer'
        db.delete_column('coupons_coupon', 'promotion_answer')

        # Deleting field 'Promotion.end_date'
        db.delete_column('coupons_promotion', 'end_date')

        # Deleting field 'Promotion.video_embed_code'
        db.delete_column('coupons_promotion', 'video_embed_code')

        # Deleting field 'Promotion.promotion_question'
        db.delete_column('coupons_promotion', 'promotion_question')


    models = {
        'coupons.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prize': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coupons.Prize']", 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coupons.Promotion']"}),
            'promotion_answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'prizes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coupons.Prize']", 'symmetrical': 'False'}),
            'promotion_question': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'video_embed_code': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['coupons']
