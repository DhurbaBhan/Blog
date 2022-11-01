from django.contrib import admin

from blogapp.models import BlogAppUser, BlogCategory, BlogPost

#showing in table view
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_title','slug')
    list_filter=("post_title",)
    search_fields=("post_title_startswith",)

# Register your models here.
admin.site.register(BlogAppUser)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(BlogCategory)

#to change site-header and indexes
admin.site.site_header = "Blog App|Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title="Dashboard"
