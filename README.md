
# Propuesta de Proyectos de Mentorías - DiploDatos 2025

# 🛰🌎 **Predicciones en Espacio: ¿Cuántos satélites y desechos podremos tener?**

## 📌 Descripción y objetivos del proyecto

En la última década hubo un crecimiento exponencial de objetos en objetos en órbita, tanto satélites como desechos espaciales. El objetivo de este proyecto es encontrar las interrelaciones entre variables, así como la sensibilidad de las mismas, además de tratar de encontrar posibles patrones relacionados a la estacionalidad y las características de los objetos que orbitan. Esto puede ser valioso permitiendo clasificar objetos en órbita y estimar la evolución de la basura espacial en el tiempo.

El proyecto busca responder las siguientes preguntas:

- **¿Cómo ha evolucionado la cantidad de satélites y desechos espaciales en los últimos años?**
- **¿Cual es la vida útil real de un satelite?**
- **¿Existen patrones en la distribución de basura espacial en diferentes órbitas?**
- **¿Qué países generan más desechos en el espacio?**
- **¿Existiran más desechos en el futuro?**
- **¿Podemos predecir la cantidad de desechos espaciales en los próximos años?**

## 🗃 Datos 

La informacion fue extraida de [Space-Track.org](https://www.space-track.org/), administrada por la fuerza aerea de Estados Unidos y [UCS Satellite Database](https://www.ucsusa.org/resources/satellite-database), que recopila informacion de diferentes agencias espaciales como NADA, ESA, CONAE, etc. El dataset esta dividos en diferentes archivos `.json`:

- `satellites.json`: contiene informacion de los satelites lanzados hasta el 02/2025.
- `debris.json`: contiene informacion de desechos orbitando hasta el 02/2025.
- `ucs-satellite-database.xlsx`: contiene informacion detallada de los satelites en funcionamiento hasta el 01/2023.

Las columnas de interes de los archivos `satellites.json` y `debris.json` son:

| **Columna**        | **Descripción** |
|--------------------|---------------|
| **OBJECT_ID**      | Identificador único asignado por NORAD. |
| **OBJECT_TYPE**    | Tipo de objeto (`PAYLOAD`, `DEBRIS`, `ROCKET BODY`, etc.). |
| **SATNAME**        | Nombre del objeto o satélite (ej. `STARLINK-3000`). |
| **COUNTRY**        | País responsable del objeto (ej. `USA`, `RUS`, `CHN`). |
| **LAUNCH**         | Fecha de lanzamiento (`YYYY-MM-DD`). |
| **SITE**           | Lugar de lanzamiento (`KSC`, `BAIKONUR`, `XICHANG`, etc.). |
| **DECAY**          | Fecha de reentrada en la atmósfera (si aplicable). Si es `NaN`, el objeto sigue en órbita. |
| **PERIOD**         | Período orbital en minutos (tiempo que tarda en dar una vuelta a la Tierra). |
| **LAUNCH_YEAR**    | Año de lanzamiento. |
| **LAUNCH_NUM**     | Número de lanzamiento de ese año. |
| **LAUNCH_PIECE**   | Letra que identifica cada objeto dentro de un mismo lanzamiento (`A`, `B`, `C`...). |
| **CURRENT**        | Estado actual del objeto (`Y` si sigue en órbita, `N` si reentró). |


Las columnas de interes del archivo `ucs-satellite-database.xlsx` son:


| **Columna**                           | **Descripción**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| **NORAD Number**                      | Número NORAD asignado al satélite para su identificación en los registros.      |
| **Current Official Name of Satellite** | Nombre oficial actual del satélite.                                              |
| **Country/Org of UN Registry**        | País o organización responsable del registro del satélite en las Naciones Unidas.|
| **Country of Operator/Owner**         | País del operador o propietario del satélite.                                    |
| **Operator/Owner**                    | Nombre del operador o propietario del satélite.                                  |
| **Users**                             | Entidades o países que hacen uso del satélite.                                   |
| **Purpose**                           | Propósito general del satélite (comunicaciones, observación, etc.).              |
| **Class of Orbit**                    | Clase de órbita en la que se encuentra el satélite (LEO, GEO, etc.).            |
| **Launch Mass (kg.)**                 | Masa total del satélite en el momento del lanzamiento (en kilogramos).           |
| **Expected Lifetime (yrs.)**          | Vida útil esperada del satélite (en años).                                       |
| **Country of Contractor**             | País donde se encuentra el contratista que fabricó el satélite.                 |
| **Launch Site**                       | Sitio o plataforma de lanzamiento del satélite.                                  |
| **Launch Vehicle**                    | Vehículo lanzador (cohete) utilizado para poner el satélite en órbita.          |


Tener dos tipos de fuentes facilita:

obtener el tamaño, orbita, proposito, vida util esperada, 