from django.contrib import admin
from .models import Post,Category,Like



class PostAdmin(admin.ModelAdmin):
    fields =['author','title','category','text','published_date','image','slug',]
    prepopulated_fields = {'slug': ('title',), }

class CategoryAdmin(admin.ModelAdmin):
    fields =['category_name',]


class LikeAdmin(admin.ModelAdmin):
    fields = ['post','user',]



admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Like,LikeAdmin)


