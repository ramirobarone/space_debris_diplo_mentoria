## Propuesta de Proyectos de Mentorías - DiploDatos 2025

# 🛰🌎 Predicciones en Espacio: ¿Cuántos satélites y desechos podremos tener?

### 📌 Descripción y objetivos del proyecto
El crecimiento exponencial de objetos en órbita, tanto satélites operativos como desechos espaciales, representa un desafío clave para la sostenibilidad del espacio. Este proyecto busca analizar, visualizar y modelar datos de satélites y fragmentos de basura espacial para comprender su evolución y prever posibles tendencias futuras.

El objetivo principal es la construcción de modelos de análisis y predicción mediante técnicas de Aprendizaje Supervisado y No Supervisado, permitiendo clasificar objetos en órbita y estimar la evolución de la basura espacial en el tiempo.

Este trabajo propone relacionar los datos satelitales con información sobre eventos clave, como colisiones, desintegraciones y lanzamientos recientes, para evaluar su impacto en la densidad orbital.

El proyecto busca responder las siguientes preguntas:

- ¿Cómo ha evolucionado la cantidad de satélites y desechos espaciales en las últimas décadas?
- ¿Existen patrones en la distribución de basura espacial en diferentes órbitas?
- ¿Qué países y empresas han contribuido más al crecimiento de satélites y fragmentos en órbita?
- ¿Podemos predecir la cantidad de desechos espaciales en los próximos años?
- ¿Qué factores pueden influir en la proliferación de basura espacial en el futuro?


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

Los datos han sido extraídos de:

[Space-Track.org](https://www.space-track.org/) - Fuente de datos oficiales sobre objetos en órbita terrestre

[UCS Satellite Database](https://www.ucsusa.org/resources/satellite-database) - Base de datos de satélites operacionales
