# 业务系统表

from django.db import models

# class BusinessSystem(models.Model):
#     id = models.AutoField(u'ID', help_text=u'ID', primary_key=True)
#     CoinCode = models.CharField(u'币种类型', help_text=u'币种类型', max_length=128, blank=True)
#
#     class Meta:
#         db_table = 'business_system'
#         verbose_name = '业务系统表'
#
#
# # ETH地址表
# class ETHAddress(models.Model):
#     id = models.AutoField(u'ID', help_text=u'ID', primary_key=True)
#     CoinCode = models.CharField(u'币种', help_text=u'币种', max_length=128, blank=True)
#     Myaddress = models.CharField(u'地址', help_text=u'地址', max_length=256, default='', blank=True)
#     create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
#     IsDelete = models.BooleanField(u'是否删除', help_text=u'是否删除', default=False, blank=True)
#
#     class Meta:
#         db_table = 'ethaddress'
#         verbose_name = 'ETH地址表'
#         ordering = ['-create_time']
#
#
# # ETH地址与业务系统表
# class ETHAddressBusinessSystem(models.Model):
#     id = models.AutoField(u'ID', help_text=u'ID', primary_key=True)
#     CoinAddr_id = models.ForeignKey('ETHAddress', verbose_name='币种地址')
#     BusinessSystem_id = models.ForeignKey('BusinessSystem', verbose_name='业务系统')
#     IsDelete = models.BooleanField(u'是否删除', help_text=u'是否删除', default=False, blank=True)
#     IsUse = models.BooleanField(u'是否使用', help_text=u'是否使用', default=False, blank=True)
#     create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
#     update_time = models.DateTimeField(u'修改时间', help_text=u'修改时间', auto_now=True)
#
#     class Meta:
#         db_table = 'eth_address_business_system'
#         verbose_name = 'ETH地址与业务系统表'
#
#
# # NEUO地址表
# class BTCAddress(models.Model):
#     id = models.AutoField(u'ID', help_text=u'ID', primary_key=True)
#     CoinCode = models.CharField(u'币种', help_text=u'币种', max_length=128, blank=True)
#     Myaddress = models.CharField(u'地址', help_text=u'地址', max_length=256, default='', blank=True)
#     create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
#     IsDelete = models.BooleanField(u'是否删除', help_text=u'是否删除', default='')
# 任务生成表
# class Create_task(models.Model):
#     id = models.AutoField(u"ID",help_text=u"ID",primary_key=True)
#     task_name = models.CharField(u"任务名称", help_text=u'任务名称',max_length=128, blank=True)
#     coin_name = models.CharField(u'币种', help_text=u'币种', max_length=128, blank=True)
#     coin_num = models.IntegerField(u'数量', help_text=u'数量', blank=True,null=True)
#     is_finish = models.BooleanField(u"是否完成",help_text=u"是否完成",default=False, blank=True)
#     create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
#     is_delete = models.BooleanField(u'是否删除', help_text=u'是否删除', default='')
#
#     class Meta:
#         db_table = 'create_task'
#         verbose_name = '任务生成表'
#         ordering = ['-create_time']



# NEO_Other地址表
# OtherAddress表\
# NEO地址表
class NEOAddress(models.Model):
    coin_type = models.CharField(max_length=256, verbose_name="币种类型")
    address = models.CharField(max_length=256)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_delete = models.BooleanField(verbose_name="是否删除", default=False,)
    is_use = models.BooleanField(verbose_name="是否使用",default=False)

    class Meta:
        db_table = 'neo_address'
        verbose_name = 'neo地址表'


# NEO_Other地址与业务系统表
class OtherAddressBusinessSystem(models.Model):

    CoinAddr_id = models.IntegerField(u"币种", help_text=u'币种',default=False, blank=True)
    BusinessSystem_id = models.IntegerField(u"系统信息", help_text=u'系统信息',default=False, blank=True )
    IsDelete = models.BooleanField(u'是否删除', help_text=u'是否删除', default=False, blank=True)
    IsUse = models.BooleanField(u'是否使用', help_text=u'是否使用', default=False, blank=True)
    create_time = models.DateTimeField(u'创建时间', help_text=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', help_text=u'修改时间', auto_now=True)

    class Meta:
        db_table = 'other_address_business_system'
        verbose_name = 'Other地址与业务系统表'


# NEO地址信息表
class NEOAddressInfo(models.Model):
    coin_type = models.CharField(max_length=128, verbose_name="币种类型", default="NEO")
    asset = models.CharField(max_length=256, verbose_name="资产类型")
    block_index = models.IntegerField(verbose_name="区块索引", default=True)
    tx_id = models.CharField(verbose_name="交易标示", max_length=256)
    create_time = models.DateTimeField(verbose_name="交易创建时间", default=True)
    address = models.CharField(max_length=256, verbose_name="地址")
    # user_id = models.IntegerField(verbose_name="用户ID")
    category = models.BooleanField(verbose_name="转入转出")
    amount = models.BigIntegerField(verbose_name="转入转出金额")

    class Meta:
        db_table = 'neo_address_info'
        verbose_name = 'neo地址表'


