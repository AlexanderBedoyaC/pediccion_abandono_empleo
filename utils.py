import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    
    return tabla

#Genera tabla de frecuencias y gráfico de barras para una variable
def univariado_barras(df, col, orientation='v'):
    
    tabla = tabla_frecuencias(df, col)
    
    fig = px.bar(tabla,
             x = col,
             y = ['Frecuencia Absoluta'],
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

#