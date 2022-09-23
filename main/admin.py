from django.contrib import admin

from .models import Category,TourSpot
# Register your models here.


admin.site.register(TourSpot)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)