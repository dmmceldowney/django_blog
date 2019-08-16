from django.contrib import admin
from .models import Post, Tag

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
