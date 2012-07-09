from django.db import models
from django.contrib import admin
from datetime import datetime

# Create your models here.
def title_first_60(self):
    return self.title[:60]

class Post(models.Model):
    title = models.CharField(max_length = 60)
    author = models.CharField(max_length = 60)
    post = models.TextField()
    date_created = models.DateField(auto_now = True,auto_now_add=True)
    date_updated = models.DateField(auto_now = True,auto_now_add=True)
    
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    author = models.CharField(max_length = 60)
    date_created = models.DateField(auto_now = True,auto_now_add=True)
    date_updated = models.DateField(auto_now = True,auto_now_add=True)
    post = models.ForeignKey(Post)
    list_display = ('title_first_60')

    def __unicode__(self):
        return self.comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_created','date_updated')
    search_fields = ('title','post')
    list_filter = ('date_created','author')
    ordering = ('title','post')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','author','post','date_created','date_updated')
    list_filter = ('date_created','author')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)   

