
![Jaws](https://i.giphy.com/media/IgqoVplwqwr8nWs3VK/giphy.gif)
# Project | data-cleaning-pandas

## Project
En este proyecto, se empieza con una base de datos de ataques de tiburones y se analizan dos hipótesis sobre estos datos:
- Hipotesis 1 _  Los ataques de tiburón han sido menos fatales(menos muertes) en los últimos años.
- Hipotesis 2 _  Los ataques de tiburón son más recurrentes en los meses de verano. 

## Cleaning
Para llegar a estas dos hipotesis:

- Exploracion y analisis de todas las columnas, ademas de las que me interesan para el estudio. Este estudio se encuentra en `exploring.ipynb`
- Hacer limpieza de los datos, para hipotesis 1, `clean-hypo1.ipynb`:
    - Modificar nombre de columnas
    - Revisar las fechas que me interesan
    - Categorizar la fatalidad y el genero. 

Hacer limpieza de los datos, para hipotesis 2, `clean-hypo2.ipynb`:
    - Coger de la fecha, el mes en que ocurrió. Deshechar valores que no tienen mes. 
    - Utilizar un pais cómo pieza para analisis de las temporadas con más ataques por tiburones.  

- Cuando tengo todos los datos necesarios, hecho todas mis tablas e imagenes de visualizaciones. `analysis.ipynb`

## Visualization

Draw at least two graphs that are insightful.
Show data that validates the conclusions based on your hypoteses in a file named 'analysis.ipynb'


#### Hypotesis extras.

1. Hipothesis 1: Los ataques de tiburón han sido menos fatales(menos muertes) en los últimos años.(¿comparativa de ratio ataques, muertes?) 
2. Hipotesis 2: Los ataques de tiburón son más recurrentes en los meses de verano. 
3. Hipotesis 3: El reporte de mujeres se ha dado en el último siglo, ya que estas no estaban vinculadas a practicas en el mar.
4. Hipotesis 4: Es el Oceano atlatico más mortifero que el Oceano pacifico? 

## Linls~References

https://www.kaggle.com/teajay/global-shark-attacks
https://numpy.org/doc/1.18/
https://pandas.pydata.org/
https://docs.python.org/3/library/functions.html
https://plotly.com/python/
https://matplotlib.org/
https://seaborn.pydata.org/
https://pandas.pydata.org/docs/
https://towardsdatascience.com/beware-of-storytelling-with-data-1710fea554b0?gi=537e0c10d89e