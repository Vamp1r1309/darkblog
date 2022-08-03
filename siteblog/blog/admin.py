from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import *



class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'author', 'category', 'views', 'get_photo', 'created_at')
    list_display_links = ('id', 'title', 'category', 'author')
    search_fields = ('title', 'content', 'author')# Search
    fields = ('title', 'slug', 'category', 'tags',  'content', 'photo', 'get_photo', 'author', 'views', 'created_at')
    readonly_fields = ('get_photo', 'views', 'created_at',)
    list_filter = ('category', 'tags')
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")
        else:
            return '-'

    get_photo.short_description = 'Фото'



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
