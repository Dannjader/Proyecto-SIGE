# Relaciones de Entidades del Proyecto

### dispositivos

- dispositivo_id **(PK)**
- tipodispositivo
- marca
- modelo 
- serial
- activoviejo
- activonuevo
- ubicacion
- id_responsable  **(FK)**
 

### dispositivos_x_servicios
- id_dxs        **(PK)**
- dispositivo_id **(FK)**
- servicio_id    **(FK)**
 
### servicios

- servicio_id **(PK)**
- tiposervicio
- fechaInicio
- fechaFin


### servicios_x_tecnicos

- id_sxt     **(PK)**
- id_equipo  **(FK)**
- id-tecnico **(FK)**


### tecnicos

- id_tecnico **(PK)**
- nombre
- apellido
- email


### responsables 

- id_responsable **(PK)**
- nombre
- cargo


### reportes

- id_reporte **(PK)**
- requerimiento
- solucion
- fechareporte

### dispositivos_x_reportes

- id_dxr         **(PK)**
- id_dispositivo **(FK)**
- id_reporte     **(FK)**


## Relaciones 
