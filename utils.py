import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

#Diccionario de datos
DATA_DICT = {
    'age': 'Edad del empleado',
    'attrition': 'Si el empleado se abandono su empleo o no el año anterior',
    'business_travel': 'Frecuencia con la que los empleados viajaron por motivos de trabajo en el último año',
    'department': 'Departamento en la empresa',
    'distance_from_home': 'Distancia del domicilio en kms',
    'education': 'Nivel de estudios',
    'education_field': 'Ámbito de formación',
    'employee_count': 'Número de empleados',
    'employee_id': 'Id de empleado',
    'gender': 'Sexo del empleado',
    'job_level': 'Nivel del puesto en la empresa en una escala de 1 a 5',
    'job_role': 'Nombre del puesto de trabajo en la empresa',
    'marital_status': 'Estado civil del empleado',
    'monthly_income': 'Ingresos mensuales en dólares al mes',
    'num_companies_worked': 'Número total de empresas en las que ha trabajado el empleado',
    'over_18': 'Si el empleado es mayor de 18 años o no',
    'percent_salary_hike': 'Porcentaje de aumento salarial en el último año',
    'standard_hours': 'Horas estándar de trabajo del empleado',
    'stock_option_level': 'Nivel de opciones sobre acciones del empleado',
    'total_working_years': 'Número total de años que el empleado ha trabajado hasta ahora',
    'training_times_last_year': 'Número de veces que se impartió formación a este empleado el año pasado',
    'years_at_company': 'Número total de años que el empleado lleva en la empresa',
    'years_since_last_promotion': 'Número de años desde el último ascenso',
    'years_with_curr_manager': 'Número de años bajo el mando del jefe actual',
    'environment_satisfaction': 'Nivel de satisfacción del entorno de trabajo',
    'job_satisfaction': 'Nivel de satisfacción laboral',
    'work_life_balance': 'Nivel de conciliación de la vida laboral y familiar',
    'job_involvement': 'Nivel de implicación en el trabajo',
    'performance_rating': 'Valoración del rendimiento en el último año',
    'mean_time': 'Tiempo promedio de trabajo al día del empleado en el último año'
}

#Genera tabla de frecuencias para una variable
def tabla_frecuencias(df, col):
    
    n = df.shape[0]
    tabla = df.groupby([col])[['employee_id']].count().rename(columns={'employee_id':'Frecuencia Absoluta'}).reset_index()
    tabla['Frecuencia Relativa'] = tabla['Frecuencia Absoluta'].apply(lambda x: str(round(100*x/n, 3))+' %')
    
    return tabla.sort_values(by='Frecuencia Absoluta', ascending=False)

#Genera tabla de frecuencias y gráfico de barras para una variable
def univariado_barras(df, col, orientation='v'):
    
    if orientation=='v':
        x = col
        y = ['Frecuencia Absoluta']
    else:
        x = ['Frecuencia Absoluta']
        y = col
    
    tabla = tabla_frecuencias(df, col)
    
    fig = px.bar(tabla,
             x = x,
             y = y,
             text_auto = True,
             title = DATA_DICT[col],
             height = 400,
             labels = {'value': 'Total', col:col},
             text = 'Frecuencia Relativa', orientation=orientation)
    fig.layout.update(showlegend=False)
    fig.show()
    
    return tabla

#Genera tabla de frecuencias y gráfico de torta para una variable
def univariado_torta(df, col, hole=0):
    
    tabla = tabla_frecuencias(df, col)
    labels = tabla[col]
    values = tabla['Frecuencia Absoluta']

    fig = go.Figure(data=[go.Pie(labels=labels,
                                values=values,
                                textinfo = 'value+percent',
                                hole = hole
                                )])
    fig.update_layout(
        title_text = DATA_DICT[col],
        height = 400 )
    fig.show()
    
    return tabla

# Definición de función que utiliza RIC para la detección de valores atípicos
def outlier_IQR(df, column, thr):
    Q1 = np.quantile(df[column], 0.25) # first quartile
    Q3 = np.quantile(df[column], 0.75) # third quartile
    IQR = Q3 - Q1 # inter - quartile range
    threshold = thr * IQR # defining the threshold
    lower = Q1 - threshold
    upper = Q3 + threshold
    lower_bound = df[df[column] < lower]
    upper_bound = df[df[column] > upper]

    #Imprimir IQR, threshold, lower bound, upper bound and total number of outlier
    print('IQR is:', IQR)
    print('Threshold is:', threshold)
    print('Lower bound is:', lower)
    print('Upper bound is:', upper)
    print('total number of outliers are:', lower_bound.shape[0] + upper_bound.shape[0])
    return upper, lower

#Imputar outliers con la mediana por grupo
def imputar_outliers(df, col, lower, upper):
    
    df_0 = df[df.attrition=='No']
    df_1 = df[df.attrition=='Yes']
    median_0 = df_0[col].median()
    median_1 = df_1[col].median()
    
    df[col] = np.where((df['attrition']=='No') & ( (df[col] < lower) | (df[col] > upper) ), median_0,
                np.where((df['attrition']=='Yes') & ( (df[col] < lower) | (df[col] > upper) ), median_1,
                df[col]))
    
    return df

#Función para esplit
def split(X, y, test_size = 0.3):
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    print('X train shape: ', X_train.shape)
    print('y train shape: ', X_test.shape)
    print('X test shape: ', y_train.shape)
    print('y test shape: ', y_test.shape)
    
    return X_train, X_test, y_train, y_test

#Pipeline para dummies y escalar variables
def transformar_datos(X):
    # Selecciona las columnas numéricas y categóricas
    numeric_features = list(X.select_dtypes(include=['int64', 'float64']).columns)
    categorical_features = list(X.select_dtypes(exclude=['int64', 'float64']).columns)

    # Combina los transformers en un ColumnTransformer
    transformer = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(), categorical_features)
        ], remainder='passthrough')

    # Crea el pipeline completo
    pipeline_transform = Pipeline(steps=[('transformer', transformer)])

    # Ajusta y transforma los datos con el pipeline
    return pipeline_transform.fit_transform(X)

#Obtener correlaciones de variables categóricas
def corr_cat(df):
    from scipy.stats import chi2_contingency
    
    cols = df.columns
    df_corr_cat = pd.DataFrame()

    corrs = []
    for col in cols:
        tabla_contingencia = pd.crosstab(df['attrition'], df[col])
        chi2, p, _, _ = chi2_contingency(tabla_contingencia)
        corrs.append(p)
    df_corr_cat['attrition'] = corrs
    df_corr_cat.index = cols
    
    return df_corr_cat