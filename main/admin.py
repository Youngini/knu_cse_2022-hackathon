from django.contrib import admin

from .models import Category,TourSpot,Option
# Register your models here.


admin.site.register(TourSpot)
admin.site.register(Option)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)