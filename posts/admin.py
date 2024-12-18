from django.contrib import admin
from .models import Post, PostFile


class PostFileInlineAdmin(admin.StackedInline):
  model = PostFile
  fields = ['file']
  extra = 0
  can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'user', 'is_active', 'created_time']
  inlines = (PostFileInlineAdmin,)

# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#   pass