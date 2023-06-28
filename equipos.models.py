# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    serial = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    activonuevo = models.CharField(db_column='activoNuevo', max_length=25)  # Field name made lowercase.
    activoviejo = models.CharField(db_column='activoViejo', max_length=25)  # Field name made lowercase.
    responsable = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'equipos'


class Trabajos(models.Model):
    id_trabajos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    fechainicio = models.DateTimeField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    id_equipos = models.OneToOneField(Equipos, models.DO_NOTHING, db_column='id_equipos')

    class Meta:
        managed = False
        db_table = 'trabajos'
