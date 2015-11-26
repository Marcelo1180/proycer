from django.contrib import admin
from models import Area, Especialidad, Nivel, Etapa
from models import Cosude, Director, Contacto, UEducativa
from models import Departamento, Provincia, Seccion, Canton, Localidad, Distrito

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'provincia')

class SeccionAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'provincia', 'seccion')

class CantonAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'provincia', 'seccion', 'canton')

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'provincia', 'seccion', 'canton', 'localidad')

class DistritoAdmin(admin.ModelAdmin):
    list_display = ('departamento', 'provincia', 'seccion', 'canton', 'localidad', 'distrito')

admin.site.register(Departamento)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Canton, CantonAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Distrito, DistritoAdmin)

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('area', 'especialidad')

class EtapaAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'etapa')

class UEducativaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'provincia', 'localidad', 'distrito', 'zona', 'direccion', 'telefonos')

admin.site.register(Cosude)
admin.site.register(Area)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Nivel)
admin.site.register(Etapa, EtapaAdmin)
admin.site.register(Director)
admin.site.register(Contacto)
admin.site.register(UEducativa, UEducativaAdmin)

# user: admin
# email: arteagamarcelo@gmail.com
# pass: Cer123