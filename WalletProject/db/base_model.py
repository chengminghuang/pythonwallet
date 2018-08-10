# -*- coding: utf-8 -*-
from django.db import models

# from control import timezone
import datetime


class BaseModel(models.Model):
    id = models.AutoField(u'ID', help_text=u'ID', primary_key=True)
    misc_desc = models.TextField(u'描述', help_text=u'描述', blank=True, default='')
    # 0.有效 1.无效 2.待审核 订单状态流程：2.处理中 0.完成 1.超过半小时无效
    STATUS_VALID = 0
    STATUS_INVALID = 1
    STATUS_REVIEW = 2

    STATUS_TYPE = (
        (STATUS_VALID, '有效'),
        (STATUS_INVALID, '无效'),
        (STATUS_REVIEW, '待审核'),
    )

    status = models.IntegerField(u'状态', help_text=u'状态', default=STATUS_REVIEW, choices=STATUS_TYPE)
    create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(u'最后修改时间', help_text=u'最后修改时间', auto_now=True)

    def __unicode__(self):
        return str(self.id)

    def update(self, validated_data):
        for field in self._meta.fields:
            val = validated_data.get(field.attname, getattr(self, field.attname, None))
            setattr(self, field.attname, val)
        return self

    class Meta:
        abstract = True