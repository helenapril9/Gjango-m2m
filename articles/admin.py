from django.contrib import admin

from .models import Article,Tag, Scope
class OrderScopeInline(admin.TabularInline):
    model = Scope
    extra = 2

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'text', 'published_at']
    inlines = [OrderScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']




