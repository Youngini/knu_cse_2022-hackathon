from django.contrib import admin

from .models import CSVtest, Category,TourSpot
# Register your models here.


admin.site.register(TourSpot)
admin.site.register(CSVtest)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)