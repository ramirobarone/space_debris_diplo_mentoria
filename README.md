# Proyecto de Mentoría - DiploDatos 2025  

# 🛰🌎 **Predicciones en el Espacio: ¿Cuántos satélites y desechos podremos tener?**  

<img src="data/images/portada.png" alt="Table" width="500"/>  

## 📌 Descripción y objetivos del proyecto  
En la última década, el número de satélites en órbita ha crecido exponencialmente debido a los avances tecnológicos y la reducción de costos de lanzamiento. Sin embargo, hay un problema que vino de la mano y que hasta hace poco tiempo no era considerado importante: los desechos espaciales. Estos desechos van desde satélites fuera de servicio hasta naves espaciales abandonadas y escombros de misiones fallidas. 

Según la NASA, actualmente hay más de 30.000 objetos rastreados en órbita, y desde 1991 se dieron tres colisiones en la órbita por culpa de los desechos. Se pronostica que, con el paso del tiempo, las dificultades se irán multiplicando. Es por esto que se necesita lograr dar una solución efectiva al asunto.

El objetivo de este proyecto es desarrollar un modelo predictivo y de clasificación de objetos en órbita terrestre. El modelado se llevará a cabo mediante técnicas de Aprendizaje Supervisado y/o No Supervisado.  

La propuesta busca analizar y correlacionar un conjunto de datos históricos que incluyen información sobre lanzamientos, satélites fuera de servicio, tamaño, órbita, período, misión, vida útil, etc., para entender su impacto en la cantidad de objetos en órbita, ya sean satélites funcionales o desechos espaciales.  

El proyecto busca responder las siguientes preguntas:  

- **¿Cómo ha evolucionado la cantidad de satélites y desechos espaciales en los últimos años?**  
- **¿Cuál es la vida útil real de un satélite?**  
- **¿Existen patrones en la distribución de basura espacial en diferentes órbitas?**  
- **¿Qué países generan más desechos en el espacio?**  
- **¿Podemos predecir la cantidad de desechos espaciales en los próximos años?**  

## 🗃 Datos  

La información fue extraída de [Space-Track.org](https://www.space-track.org/), administrado por la Fuerza Aérea de los Estados Unidos, y del [UCS Satellite Database](https://www.ucsusa.org/resources/satellite-database), que recopila datos de diferentes agencias espaciales como NASA, ESA, CONAE, entre otras.  

El dataset está dividido en diferentes archivos:  

- `satellites.json`: contiene información de los satélites lanzados hasta febrero de 2025.  
- `debris.json`: incluye datos sobre desechos espaciales en órbita hasta febrero de 2025.  
- `ucs-satellite-database.xlsx`: proporciona información detallada de los satélites en funcionamiento hasta enero de 2023.  

### Variables principales  

**Archivos `satellites.json` y `debris.json`**  

| **Columna**        | **Descripción** |
|--------------------|---------------|
| **OBJECT_ID**      | Identificador único asignado por NORAD. |
| **OBJECT_TYPE**    | Tipo de objeto. |
| **SATNAME**        | Nombre del objeto o satélite. |
| **COUNTRY**        | País responsable del objeto. |
| **LAUNCH**         | Fecha de lanzamiento. |
| **SITE**           | Lugar de lanzamiento. |
| **DECAY**          | Fecha de reentrada en la atmósfera. |
| **PERIOD**         | Período orbital en minutos. |
| **LAUNCH_YEAR**    | Año de lanzamiento. |
| **LAUNCH_NUM**     | Número de lanzamiento de ese año. |
| **LAUNCH_PIECE**   | Letra que identifica cada objeto dentro de un mismo lanzamiento. |
| **CURRENT**        | Estado actual del objeto. |  

**Archivo `ucs-satellite-database.xlsx`**  

| **Columna**                           | **Descripción**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| **NORAD Number**                      | Identificador único asignado por NORAD. |
| **Current Official Name of Satellite** | Nombre oficial del satélite. |
| **Country of Operator/Owner**         | País del operador o propietario del satélite. |
| **Operator/Owner**                    | Nombre del operador o propietario del satélite. |
| **Users**                             | Entidades o países que utilizan el satélite. |
| **Purpose**                           | Propósito general del satélite. |
| **Class of Orbit**                    | Órbita en la que se encuentra el satélite. |
| **Launch Mass (kg.)**                 | Masa del satélite en el momento del lanzamiento. |
| **Expected Lifetime (yrs.)**          | Vida útil esperada. |
| **Country of Contractor**             | País donde se encuentra el fabricante. |
| **Launch Site**                       | Sitio del lanzamiento. |
| **Launch Vehicle**                    | Lanzador. |  

El uso de estas dos fuentes de datos permite obtener información clave sobre:  
- Tamaño y masa de los satélites.  
- Órbita según el período orbital.  
- Propósito de cada satélite (para qué fue fabricado).  
- Vida útil esperada de los satélites.  

## 💻 Desarrollo 

El desarrollo de este proyecto se divide de la siguiente manera: 

1. [Análisis y Visualización](docs/analisis_y_visualizacion.md)
2. Análisis Exploratorio y Curación de Datos
3. Aprendizaje Supervisado y/o No Supervisado