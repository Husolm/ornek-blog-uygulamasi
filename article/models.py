from enum import auto
from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_images = models.FileField(blank=True,null = True,verbose_name="Makaleye fotoğraf ekleyin:")
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="isim")
    comment_content = models.CharField(max_length=200,verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

