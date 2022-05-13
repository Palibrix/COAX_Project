from django.contrib import admin

from .models import Cities, Hospitals, Departments, Doctor

# admin.site.register(Cities)
# admin.site.register(Hospitals)
admin.site.register(Departments)
admin.site.register(Doctor)

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('city', 'region')
    ordering = ('-region',)
    search_fields = ('city', 'region')



@admin.register(Hospitals)
class HospitalsAdmin(admin.ModelAdmin):
    list_display =('hospital_name', 'region')
    ordering = ("-region",)
