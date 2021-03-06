from django.db import models
from geoposition.fields import GeopositionField
from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django.contrib.auth.models import User

class Departamento(models.Model):
    departamento = models.CharField(max_length=50)

    def __str__(self):
		return self.departamento

    def __unicode__(self):
        return self.departamento

class Provincia(models.Model):
    departamento = models.ForeignKey(Departamento)
    provincia = models.CharField(max_length=150)

    def __str__(self):
		return self.provincia

    def __unicode__(self):
        return self.provincia

class Seccion(models.Model):
    departamento = models.ForeignKey(Departamento)
    provincia = ChainedForeignKey(Provincia, chained_field="departamento", chained_model_field="departamento")
    seccion = models.CharField(max_length=150)

    def __str__(self):
		return self.seccion

    def __unicode__(self):
        return self.seccion

class Canton(models.Model):
    departamento = models.ForeignKey(Departamento)
    provincia = ChainedForeignKey(Provincia, chained_field="departamento", chained_model_field="departamento")
    seccion = ChainedForeignKey(Seccion, chained_field="provincia", chained_model_field="provincia")
    canton = models.CharField(max_length=150)

    def __str__(self):
		return self.canton

    def __unicode__(self):
        return self.canton

class Localidad(models.Model):
    departamento = models.ForeignKey(Departamento)
    provincia = ChainedForeignKey(Provincia, chained_field="departamento", chained_model_field="departamento")
    seccion = ChainedForeignKey(Seccion, chained_field="provincia", chained_model_field="provincia")
    canton = ChainedForeignKey(Canton, chained_field="canton", chained_model_field="canton")
    localidad = models.CharField(max_length=150)

    def __str__(self):
		return self.localidad

    def __unicode__(self):
        return self.localidad

class Distrito(models.Model):
    departamento = models.ForeignKey(Departamento)
    provincia = ChainedForeignKey(Provincia, chained_field="departamento", chained_model_field="departamento")
    seccion = ChainedForeignKey(Seccion, chained_field="provincia", chained_model_field="provincia")
    canton = ChainedForeignKey(Canton, chained_field="canton", chained_model_field="canton")
    localidad = ChainedForeignKey(Localidad, chained_field="localidad", chained_model_field="localidad")
    distrito = models.CharField(max_length=150)

    def __str__(self):
		return self.distrito

    def __unicode__(self):
        return self.distrito

class Area(models.Model):
    area = models.CharField(max_length=50)

    def __str__(self):
		return self.area

    def __unicode__(self):
        return self.area

class Especialidad(models.Model):
    area = models.ForeignKey(Area)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
		return "%s - %s" % (self.area, self.especialidad)

    def __unicode__(self):
        return "%s - %s" % (self.area, self.especialidad)

class Nivel(models.Model):
    nivel = models.CharField(max_length=50)

    def __str__(self):
		return self.nivel

    def __unicode__(self):
        return self.nivel

class Etapa(models.Model):
    nivel = models.ForeignKey(Nivel)
    etapa = models.CharField(max_length=50)

    def __str__(self):
		return  "%s - %s" % (self.nivel, self.etapa)

    def __unicode__(self):
        return  "%s - %s" % (self.nivel, self.etapa)

class Director(models.Model):
    nombres = models.CharField(max_length=70)
    paterno = models.CharField(max_length=70)
    materno = models.CharField(max_length=70)
    ci = models.CharField(max_length=10)
    rda = models.CharField(max_length=10)
    formacion = models.TextField()
    especialidad = models.TextField()

class Contacto(models.Model):
    nombres = models.CharField(max_length=70)
    parteno = models.CharField(max_length=70)
    materno = models.CharField(max_length=70)
    ci = models.CharField(max_length=10)
    telefonos = models.CharField(max_length=50)
    email = models.EmailField()

class Cosude(models.Model):
    cosude = models.CharField(max_length=10)

    def __str__(self):
		return  self.cosude

    def __unicode__(self):
        return  self.cosude

DEPENDENCIA_CHOICE = (
    ('F', 'Fiscal'),
    ('P', 'Privada'),
    ('C', 'Convenio'),
)
AREA_CHOICE = (
    ('R', 'Rural'),
    ('U', 'Urbana'),
)
BOOL_CHOICES = (
    (True, 'Si'),
    (False, 'No')
)

class UEducativa(models.Model):
    cosude = models.ForeignKey(Cosude)
    codigo = models.CharField(max_length=10)
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    zona = models.CharField(max_length=100)
    direccion = models.TextField()
    dependencia = models.CharField(max_length=1, choices=DEPENDENCIA_CHOICE)
    area = models.CharField(max_length=1, choices=AREA_CHOICE)
    nombre = models.CharField(max_length=100)
    telefonos = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    email = models.EmailField(default='')
    year_fundation = models.IntegerField()
    coordenadas = GeopositionField()
    # DIRECTOR
    director = models.OneToOneField(Director)
    # SERVICIOS EDUCATIVOS
    etapa = models.ManyToManyField(Etapa)
    especialidad = models.ManyToManyField(Especialidad)
    # INTERNET INSTITUCIONAL
    internet = models.BooleanField(choices=BOOL_CHOICES)
    imagen = models.ImageField(upload_to='uploads/ueducativa')
    video = models.URLField()
    link_institucional = models.URLField()
    # CANTIDAD DE PERSONAL
    cant_estudiantes = models.IntegerField()
    cant_docentes = models.IntegerField()
    cant_administrativos = models.IntegerField()
    # CONTACTOS
    contacto = models.OneToOneField(Contacto)
    # USUARIOS
    # user = models.ForeignKey(User)