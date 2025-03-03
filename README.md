
# Propuesta de Proyectos de Mentorías - DiploDatos 2025

# 🛰🌎 **Predicciones en Espacio: ¿Cuántos satélites y desechos podremos tener?**

<img src="https://github.com/EnzoRg/space_debris/blob/main/image/portada.png" alt="Table" width="500"/>

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

La informacion fue extraida de [Space-Track.org](https://www.space-track.org/), administrado por la fuerza aérea de Estados Unidos y [UCS Satellite Database](https://www.ucsusa.org/resources/satellite-database), que recopila informacion de diferentes agencias espaciales como NASA, ESA, CONAE, etc. El dataset esta dividos en diferentes archivos:

- `satellites.json`: contiene informacion de los satelites lanzados hasta el 02/2025.
- `debris.json`: contiene informacion de desechos orbitando hasta el 02/2025.
- `ucs-satellite-database.xlsx`: contiene informacion detallada de los satelites en funcionamiento hasta el 01/2023.

Las columnas más relevantes de los archivos `satellites.json` y `debris.json` son:

| **Columna**        | **Descripción** |
|--------------------|---------------|
| **OBJECT_ID**      | Identificador único asignado por NORAD |
| **OBJECT_TYPE**    | Tipo de objeto |
| **SATNAME**        | Nombre del objeto o satélite |
| **COUNTRY**        | País responsable del objeto |
| **LAUNCH**         | Fecha de lanzamiento |
| **SITE**           | Lugar de lanzamiento |
| **DECAY**          | Fecha de reentrada en la atmósfera |
| **PERIOD**         | Período orbital en minutos |
| **LAUNCH_YEAR**    | Año de lanzamiento |
| **LAUNCH_NUM**     | Número de lanzamiento de ese año |
| **LAUNCH_PIECE**   | Letra que identifica cada objeto dentro de un mismo lanzamiento |
| **CURRENT**        | Estado actual del objeto |


Las columnas más relevantes del archivo `ucs-satellite-database.xlsx` son:


| **Columna**                           | **Descripción**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| **NORAD Number**                      | Identificador único asignado por NORAD |
| **Current Official Name of Satellite** | Nombre oficial del satélite |
| **Country of Operator/Owner**         | País del operador o propietario del satélite |
| **Operator/Owner**                    | Nombre del operador o propietario del satélite |
| **Users**                             | Entidades o países que usan el satélite |
| **Purpose**                           | Propósito general del satélite |
| **Class of Orbit**                    | Órbita en la que se encuentra el satélite |
| **Launch Mass (kg.)**                 | Masa del satélite en el momento del lanzamiento |
| **Expected Lifetime (yrs.)**          | Vida útil esperada |
| **Country of Contractor**             | País donde se encuentra el fabricante |
| **Launch Site**                       | Sitio del lanzamiento |
| **Launch Vehicle**                    | Lanzador |


Tener dos fuentes de datos permite obtener: 

- Tamaño y masa
- Órbita segun el periodo orbital
- Proposito de cada satelite (para que se fabrico)
- Vida util esperada
