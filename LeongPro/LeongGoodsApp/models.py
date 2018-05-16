from django.db import models
import datetime

# Create your models here.

class TypeInfo(models.Model):
    '''商品分类'''
    t_title  = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        '''显示汉字'''
        return self.t_title.encode('utf8')


class GoodsInfo(models.Model):
    '''商品'''
    g_title  = models.CharField(max_length=20)
    g_pic    = models.ImageField(upload_to='/static/media/')
    iaDelete = models.BooleanField(default=False)
    g_price  = models.DecimalField(max_digits=5, decimal_places=2)
    g_type   = models.ForeignKey(TypeInfo)
    g_click  = models.IntegerField(default=0)
    #g_unit   = models.CharField(max_length=20, default='500g')  #单位
    g_unit   = models.IntegerField(default='500')
    g_jianji = models.TextField()
    pub_date = models.DateTimeField(datetime.datetime.now())
    pubg_date = models.DateTimeField()

    def __str__(self):
        return self.g_title.encode('utf8')