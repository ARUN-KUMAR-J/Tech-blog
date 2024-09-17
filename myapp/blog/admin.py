from django.contrib import admin
from .models import Posts,Category,aboutus

class PostAdmin(admin.ModelAdmin):
    search_fields =('title','content')
    list_filter = ('category_id','created')
    

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)
admin.site.register(aboutus)
# Register your models here.
