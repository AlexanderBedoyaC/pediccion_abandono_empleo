# Prediccion abandono empleo

La agencia de marketing Sterling Cooper Advertising tiene en su planta de empleados alrededor de
4.000 personas directamente contratadas. Sin embargo, el departamento de recursos humanos ha
reportado cifras preocupantes a la dirección de la agencia, indicando que cada año, alrededor del
15% de sus empleados abandonan la empresa y necesitan ser reemplazados, en la mayoría de casos,
con muy poco tiempo para el proceso de selección y contratación. La dirección cree que este nivel
de bajas (empleados que se marchan, ya sea por decisión propia o porque son despedidos) es
perjudicial para la empresa, por las siguientes razones:

- Los proyectos de los antiguos empleados se retrasan, lo que dificulta el cumplimiento de los
plazos, con la consiguiente pérdida de reputación entre sus clientes y socios.

- El departamento de recursos humanos requiere mucha inversión por los niveles de rotación,
así que la mayoría de su personal está dedicado a tareas de reclutamiento de nuevo talento,
haciendo más lento el proceso de desarrollo de otras áreas dentro del departamento
dedicadas por ejemplo a la formación o bienestar de sus empleados.

- En la mayoría de los casos, hay que formar a los nuevos empleados para el puesto y/o darles
tiempo para que se adapten a la cultura de la agencia.

Por ello, la dirección ha contratado a su equipo de consultores para saber en qué factores deben
centrarse para frenar el abandono de empleados. En otras palabras, quieren predecir a tiempo si sus
empleados van a abandonar su empleo para tomar acciones preventivas que les permita retener a la
mayoría de los empleados en riesgo. También quieren saber cuál de estas variables es la más
importante y debe abordarse de inmediato.

# Diseño de solución propuesto


Para abordar este problema se cuenta con información general del empleado, resultados de encuesta 
realizada a los empleados respecto a su nivel de satisfacción con su empleo actual, resultados 
obtenidos por los empleados en su última evaluación de desempeño y el tiempo promedio de dedicación 
del empleado al día.

Primeramente, se busca entender los datos disponibles sobre los empleados de la empresa para encontrar 
patrones y relaciones que nos permitan saber qué está sucediendo. El objetivo es extraer de los datos 
la mayor y más relevante información posible para con esto aplicar diferentes algoritmos supervisados 
de shallow learning que permitan a la empresa predecir a tiempo si sus empleados van a abandonar su 
empleo, y así poder tomar acciones preventivas que les permita retener a la mayoría de los empleados en riesgo.

A continuación, se detalla aún más el diseño de solución:

## Análisis de Datos y Negocio

**Limpieza y Transformación de los Datos**
- Llevar a cabo una limpieza de datos para tratar valores faltantes o anómalos.
- Transformar los datos para que estén listos para el análisis, como codificar variables categóricas.

**Análisis Exploratorio de los Datos (EDA)**
- Realizar un EDA para comprender mejor los datos. Esto incluye estadísticas descriptivas, gráficos y
  visualizaciones.
- Identificar patrones en los datos, como correlaciones entre variables y distribuciones relevantes.

**Preparación de los Datos**
- Realizar una codificación one-hot para variables categóricas y lo necesario para que los datos puedan
  ser suministrados a los algoritmos.

**Selección de Variables**
- Utilizar técnicas como la matriz de correlación y la importancia de características para seleccionar
  las variables más relevantes.
- Evaluar si es necesario crear nuevas características basadas en el análisis exploratorio.

## Machine Learning

**Selección de variables**
- Utilizar diferentes técnicas robustas de selección de variables y regularización para disminuir el número
  de características.

**Comparar resultados de los diferentes métodos de selección de variables**
- Utilizar una Regresión Logistica y un Bosque Aleatorio para casificación para evaluar el rendimiento y
  escoger las mejores selecciones de variables.

**Aplicación de Algoritmos/Técnicas de Modelado**
- Seleccionar algoritmos adecuados para abordar el problema, como Regresión Logística, Random Forest Classifier,
  Gradient Boosting y Support Vector Machine.

**Comparación y Selección de Técnicas**
- Evaluar los diferentes modelos y técnicas de clasificación utilizando métricas de rendimiento como precisión,
  recall, F1-score y acurracy.
- Comparar modelos para identificar los más efectivos en la predicción de la rotación.

**Afinamiento de Hiperparámetros**
- Realizar la optimización de hiperparámetros para mejorar el rendimiento de los modelos seleccionados.
- Utilizar técnicas como la búsqueda de cuadrícula (Grid Search) o búsqueda aleatoria (Randomized Search) para
  encontrar los mejores hiperparámetros.

**Evaluación y Análisis del Mejor Modelo**
- Evaluar los dos mejores modelos con los hiperparámetros encontrados para cada uno y seleccionar el mejor.
- Realizar un análisis de importancia de características para comprender qué variables influyen más en las predicciones.
- Interpretar los resultados del modelo para obtener información sobre qué características aumentan la probabilidad de rotación.

## Conclusiones Finales y Recomendaciones
- Resumir los hallazgos y conclusiones del proyecto.
- Proporcionar recomendaciones basadas en el análisis para reducir la rotación de empleados, como mejoras en el entorno
  de trabajo, ajustes salariales, programas de capacitación, etc.

Este enfoque combina análisis de datos, técnicas de machine learning y un enfoque de negocio para abordar el problema de 
la rotación de empleados y tomar decisiones informadas para reducir este problema en la empresa.
