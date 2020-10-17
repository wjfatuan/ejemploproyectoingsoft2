from django.contrib import admin

from .models import Ciudad, Aeropuerto, Vuelo

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id','codigo','pais', 'nombre')
    fields = ('pais','nombre','codigo',)

# Register your models here.
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Aeropuerto)
admin.site.register(Vuelo)
