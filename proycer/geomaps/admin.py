from django.contrib import admin
from models import Area, Especialidad, Nivel, Etapa
from models import Director, Contacto, UEducativa

class UEducativaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'provincia', 'localidad', 'distrito', 'zona', 'direccion', 'telefonos')

admin.site.register(Area)
admin.site.register(Especialidad)
admin.site.register(Nivel)
admin.site.register(Etapa)
admin.site.register(Director)
admin.site.register(Contacto)
admin.site.register(UEducativa, UEducativaAdmin)

# user: admin
# email: arteagamarcelo@gmail.com
# pass: Cer123