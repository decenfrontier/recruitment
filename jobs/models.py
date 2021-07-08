from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    JobTypes = [
        (0, '技术类'),
        (1, '产品类'),
        (2, '运营类'),
        (3, '设计类'),
    ]
    Cities = [
        (0, '北京'),
        (1, '上海'),
        (2, '深圳'),
    ]
    type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='职位类别')
    name = models.CharField(max_length=100, blank=False, verbose_name='职位名称')
    city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name='工作地点')
    responsibility = models.TextField(max_length=1024, verbose_name='职位职责')
    requirement = models.TextField(max_length=1024, blank=False, verbose_name='职位要求')
    creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='修改时间', default=datetime.now)