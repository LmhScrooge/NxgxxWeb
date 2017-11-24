# -*- coding:UTF-8 -*-
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题名称',max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,verbose_name='问题')
    choice_text = models.CharField('选项',max_length=200)
    votes = models.IntegerField('投票数',default=0)

    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'