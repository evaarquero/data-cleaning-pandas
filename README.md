[!gif](https://i.giphy.com/media/IgqoVplwqwr8nWs3VK/giphy.gif)


# Project | data-cleaning-pandas

En este proyecto, se empieza con una base de datos de ataques de tiburones y se analizan dos hipótesis sobre estos datos:
- Hipotesis 1 _  Los ataques de tiburón han sido menos fatales(menos muertes) en los últimos años.
- Hipotesis 2 _  Los ataques de tiburón son más recurrentes en los meses de verano. 

Para llegar a estas dos hipotesis:

- Exploracion y analisis de todas las columnas, ademas de las que me interesan para el estudio. Este estudio se encuentra en "Exploring.ipynb"
- Hacer limpieza de los datos:
    - Modificar nombre de columnas
    - Revisar las fechas que me interesan
    - Categorizar la fatalidad y el genero. 
    - Coger de la fecha, el mes en que ocurrió. Deshechar valores que no tienen mes. 
    - Utilizar un pais cómo pieza para analisis de las temporadas con más ataques por tiburones.  
- Cuando tengo todos los datos necesarios, hecho todas mis tablas e imagenes a visualizaciones. "visualizations.ipynb"


## Hypothesis
Decide a hypothesis (or hypotheses) with which you will clean the data

1. Hipothesis 1: Los ataques de tiburón han sido menos fatales(menos muertes) en los últimos años.(¿comparativa de ratio ataques, muertes?) 
2. Hipotesis 2: El reporte de mujeres se ha dado en el último siglo, ya que estas no estaban vinculadas a practicas en el mar. 
3. Hipotesis 3: Hay zonas que son más recurrentes por los tiburones, según la temporada.
4. Hipotesis 4: Es el Oceano atlatico más mortifero que el Oceano pacifico? 
5. Hipotesis 5: Los ataques son más usuales en la cosa este de australia, por el ratio de población o densidad de tiburones. 

## Exploring

Explore the data and write down what you have found. 
Con un primer vistazo, vemos:
- De 25723 entries, hay 17021 nulos (Minimo), teniendo en cuenta que el Cas number  o la fecha son los más importantes. 
- We can see that there are a seies of data, which are without case number and data. 
- Therefore there´s a possibility for purge all rows, in which there is no information given
- Hay dos columnas con solo un dato, estas no presentarán ningún valor a la estadistica. (se borrarán más adelante)
### Descubriendo columnas y entendiendo su información
#### 1.1 CASE NUMBER / DATES / YEAR
Estas tres columnas están relacionadas, ya que se basan en la fecha en la que ocurrió o se reportó.
From the dictionary of Dates:
- It can be seen that dates are repeated by two sometimes, I checked that this is casuall
- There are some dates that are "reported" which are related to the case number ending in R (2017.11.25.R)
- Fechas que tienene el año como 144, que en realidad se refieren al 1944 (mirando el case number o el year)
- Estas fechas suelen estar contrastadas y corregidas en la columna "Year".
- como fecha se da la World War II
Sería posible incluso buscar estás fechas "erroneas"
#### 1.2 Type
Viendo el type viene esta pregunta : ¿qué quiere decir con "Type" en la columna?
- Provoked = que de alguna manera los han provocado.(acercandose a los tiburones,  etc)
- Invalid ?? = 
- Sea Disaster - algun tipo de hundimiento, accidente aereo, etc
- Boating = Pescando, iendo en bote, canoa, kayak... etc
- Questionable = hay dos surfers
- Boatomg = 1 fishing 

Could be said that this is a category, having: 
- Provoked
- Unprovoked + Questionable + boating + boat
- Sea Disaster

Is it the sex related to this accidents? 
#### 1.3 Country / Area / location
Estas tres columnas tambien están relacionadas. 

Los paises más atacados por sharks son USA y AUSTRALIA. 

### 1.3 Country / Area / location
Estas tres columnas tambien están relacionadas. 

Los paises más atacados por sharks son USA y AUSTRALIA. 

#### 1.4 Name / Sex
EL nombre de la columna es "Sex ", cambiar a "Sex".
- A veces en sexo pone N, porque son dos personas de distinto sexo  (luego hay otro que es un hombre)
- Si está en blanco o con "." significa que no tienene el nombre. 
- Cambiar variables como:  "M " a "M", "lli" a "M"

Esta categoría, sin mirarla muy de cerca podría verse bien dos categorias facilmente limpiables (Male y Female)

Hay unos 5737 datos de genero. Que según mi criterio es una buena manera de empezar. 

#### 1.5 Species
En "Species " vemos 3464 datos de los que podrian ser 6000, esto quiere decir que habrá muchos datos sin poder saber la especie.

- Descubrimos que hay algunas datos en los que se dice que los tiburones no estaban confirmados.
- Se tieneen muchos tipos, muy mal ordenados. Esta lista no nos sirve como categoria 

lista de sharks no confirmados:
"""
 'Shark involvement suspected but not confirmed': 4,
 'Shark involvement questionable': 4,
 'Shark involvement prior to death was not confirmed': 105,
 'Invalid': 102,
 'Shark involvement not confirmed': 88,
 'Questionable incident': 35,
 'Questionable': 34,
 'No shark involvement': 21,
 'Shark involvement prior to death not confirmed': 13,
 'Shark involvement suspected but not confirmed': 4,
 'Shark involvement questionable': 4,
 'Questionable Incident': 3,
 'Shark involvement not cofirmed': 2 """



## Cleaning

Use at least 5 data cleaning techniques inside a file named clean.ipynb
null values, columns drop, duplicated data, string manipulation, apply fn, categorize, regex, etc.

## Visualization

Draw at least two graphs that are insightful.
Show data that validates the conclusions based on your hypoteses in a file named 'analysis.ipynb'

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