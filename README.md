# space_debris

## Descripción de las Columnas  

| **Columna**        | **Descripción** |
|--------------------|---------------|
| **INTLDES**        | **Diseño Internacional** del lanzamiento en formato `YYNNNA` (Año, Número, Pieza). Ejemplo: `1998-067A` (ISS Zarya). |
| **NORAD_CAT_ID**   | **Número de catálogo NORAD**, identificador único de cada objeto espacial. |
| **OBJECT_TYPE**    | Tipo de objeto (`PAYLOAD`, `DEBRIS`, `ROCKET BODY`, etc.). |
| **SATNAME**        | Nombre del objeto o satélite (ej. `STARLINK-3000`). |
| **COUNTRY**        | País responsable del objeto (ej. `USA`, `RUS`, `CHN`). |
| **LAUNCH**         | Fecha de lanzamiento (`YYYY-MM-DD`). |
| **SITE**           | Lugar de lanzamiento (`KSC`, `BAIKONUR`, `XICHANG`, etc.). |
| **DECAY**          | Fecha de reentrada en la atmósfera (si aplicable). Si es `NaN`, el objeto sigue en órbita. |
| **PERIOD**         | Período orbital en minutos (tiempo que tarda en dar una vuelta a la Tierra). |
| **INCLINATION**    | Inclinación orbital en grados (`0°` es ecuatorial, `90°` es polar). |
| **APOGEE**         | Altitud máxima de la órbita en km (punto más alejado de la Tierra). |
| **PERIGEE**        | Altitud mínima de la órbita en km (punto más cercano a la Tierra). |
| **COMMENT**        | Notas sobre el objeto (puede estar vacío). |
| **COMMENTCODE**    | Código numérico asociado a un comentario (cuando existe). |
| **RCSVALUE**       | Código de reflectividad de radar del objeto (útil para estimar su tamaño). |
| **RCS_SIZE**       | Tamaño estimado del objeto según su reflectividad (`Small`, `Medium`, `Large`). |
| **FILE**           | Número de archivo de Space-Track asociado al objeto. |
| **LAUNCH_YEAR**    | Año de lanzamiento. |
| **LAUNCH_NUM**     | Número de lanzamiento de ese año. |
| **LAUNCH_PIECE**   | Letra que identifica cada objeto dentro de un mismo lanzamiento (`A`, `B`, `C`...). |
| **CURRENT**        | Estado actual del objeto (`Y` si sigue en órbita, `N` si reentró). |
| **OBJECT_NAME**    | Nombre del objeto en registros oficiales. |
| **OBJECT_ID**      | Identificador único asignado por NORAD. |
| **OBJECT_NUMBER**  | Número de objeto en la base de datos de Space-Track. |
