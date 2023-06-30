# Entidades del Proyecto

### Dispositivos

- dispositivo_id **(PK)**
- tipoDispositivo
- marca
- modelo 
- serial
- activoViejo
- activoNuevo
- ubicacion

### Servicios

- servicios_id **(PK)**
- tipoServicio
- fechaInicio
- fechaFin

### Tecnicos

- id_tecnico **(PK)**
- nombre
- apellido
- email


### Responsables

- id_responsable **(PK)**
- nombre
- cargo


### Reportes

- id_reporte **(PK)**
- requerimiento
- solucion
- fechaReporte

