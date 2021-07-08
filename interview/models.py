from django.db import models

class Candidate(models.Model):
    # 基础信息
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name='应聘者ID')
    username = models.CharField(max_length=20, verbose_name='姓名')
    city = models.CharField(max_length=20, verbose_name='城市')
    phone = models.CharField(max_length=20, verbose_name='手机号码')
    email = models.EmailField(max_length=50, blank=True, verbose_name='邮箱')
    apply_position = models.CharField(max_length=50, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(max_length=50, blank=True, verbose_name='生源地')

    # TODO
    ...