
# @Date    : 2016-11-26 18:54:49
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1
# from __future__ import unicode_literals

from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
# import ast

#第四
class Article(models.Model):
    title = models.CharField('标题', max_length=256)
    content = models.TextField('内容')

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('更新时间',auto_now=True, null=True)




#第三
# @python_2_unicode_compatible
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     qq = models.CharField(max_length=10)
#     # addr = models.TextField('北京')
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# @python_2_unicode_compatible
# class Article(models.Model):
#     title = models.CharField(max_length=50)
#     author = models.ForeignKey(Author)
#     content = models.TextField()
#     score = models.IntegerField()  # 文章的打分
#     tags = models.ManyToManyField('Tag')
#
#     def __str__(self):
#         return self.title
#
#
# @python_2_unicode_compatible
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name







#第二
# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):  # __str__ on Python 3
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#
#     def __str__(self):  # __str__ on Python 3
#         return self.name
#
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):  # __str__ on Python 3
#         return self.headline
#
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#     def __str__(self):
#         return self.name
#
#


#第一
# class CompressedTextField(models.TextField):
#     """
#     model Fields for storing text in a compressed format (bz2 by default)
#     """
#
#     def from_db_value(self, value, expression, connection, context):
#         if not value:
#             return value
#         try:
#             return value.decode('base64').decode('bz2').decode('utf-8')
#         except Exception:
#             return value
#
#     def to_python(self, value):
#         if not value:
#             return value
#         try:
#             return value.decode('base64').decode('bz2').decode('utf-8')
#         except Exception:
#             return value
#
#     def get_prep_value(self, value):
#         if not value:
#             return value
#         try:
#             value.decode('base64')
#             return value
#         except Exception:
#             try:
#                 return value.encode('utf-8').encode('bz2').encode('base64')
#             except Exception:
#                 return value
#
# class ListField(models.TextField):
#     __metaclass__ = models.base
#     description = "Stores a python list"
#
#     def __init__(self, *args, **kwargs):
#         super(ListField, self).__init__(*args, **kwargs)
#
#     def to_python(self, value):
#         if not value:
#             value = []
#
#         if isinstance(value, list):
#             return value
#
#         return ast.literal_eval(value)
#
#     def get_prep_value(self, value):
#         if value is None:
#             return value
#
#         return str(value) # use str(value) in Python 3
#
#     def value_to_string(self, obj):
#         value = self._get_val_from_obj(obj)
#         return self.get_db_prep_value(value)
#
#
# class Article(models.Model):
#     labels = ListField()