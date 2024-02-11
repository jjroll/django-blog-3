from django.contrib import admin

from blogging.models import Post, Category

class CategoriesInline(admin.TabularInline):
    model = Category.posts.through    

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline]

# and a new admin registration
admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)
