# Proyecto de Mentoría - DiploDatos 2025  

# 🛰🌎 **Predicciones en el Espacio: ¿Cuántos satélites y desechos podremos tener?**  

<img src="data/images/portada.png" alt="Portada desechos espaciales" width="500"/>  

## 📌 Descripción y objetivos del proyecto  
En la última década, el número de satélites en órbita ha crecido exponencialmente debido a los avances tecnológicos y la reducción de costos (New Space). Sin embargo, hay un problema que vino de la mano y que hasta hace poco tiempo no era considerado importante: **los desechos espaciales**. Estos desechos van desde satélites fuera de servicio hasta naves espaciales abandonadas y escombros de misiones fallidas. 

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
- `rockets.json`: incluye datos sobre los lanzadores en órbita hasta febrero de 2025. 
- `unknown.json`: incluye datos sobre objetos no identificados en órbita hasta febrero de 2025. 
- `ucs-satellite-database.xlsx`: proporciona información detallada de los satélites en funcionamiento hasta enero de 2023.  

## 💻 Desarrollo 

El desarrollo de este proyecto se divide de la siguiente manera: 

- [Introducción a los Satélites](docs/intro_satelites.md)
- [Descripción de los Datos](docs/dataset.md)
- [Análisis y Visualización](docs/analisis_y_visualizacion.md)
- [Análisis Exploratorio y Curación de Datos](docs/analisis_exploratorio.md)
- [Aprendizaje Supervisado y/o No Supervisado](docs/aprendizaje.md)
- [Resultados y Conclusiones](docs/resultados.md)

## 📚 Referencias
- [Space-Track API](https://www.space-track.org/documentation#/api)
- [ISS Tracker](https://isstracker.pl/en)
- [How many satellites can we safely fit in Earth orbit?](https://www.n2yo.com/satellite-article/How-many-satellites-can-we-safely-fit-in-Earth-orbit/86)

</b><p align="center"><sup> EnzoRg | </sup><a href="../README.md"><sup>Contenidos</sup></a></p>