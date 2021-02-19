from django.contrib import admin
from .models import Category, Product, Images

# Register your models here.

admin.site.register(Category)



class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

admin.site.register(Images)





class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)