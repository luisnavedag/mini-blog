from django.contrib import admin
from .models import Blog,EditorForm


admin.site.site_header = "Mini-Blog Admin"
admin.site.site_title = "Mini-Blog Admin"
admin.site.index_title = "Welcome to Mini-Blog Dashboard"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/admin/main.js',)
    
@admin.register(EditorForm)
class EditorFormAdmin(admin.ModelAdmin):
    list_display = ['subject','user','message','portfolio_url','created_at']