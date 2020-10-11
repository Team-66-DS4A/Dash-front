import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64


## Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px

casos_positivos = pd.read_excel('Data/positivos_24_09_2020.xlsx', sheet_name= 'casos_positivos')
casos_positivos['Egreso'] = casos_positivos['Egreso'].replace('Recuperado_tiempo','Recuperado')
casos_positivos = casos_positivos.drop(['pri_nom_', 'seg_nom_', 'pri_ape_','seg_ape_'], axis = 1)
casos_positivos = casos_positivos.drop(['ORDEN'], axis = 1)
casos_positivos = casos_positivos[['Identificacion', 'Fecha', 'SEMANA', 'año', 'Edad', 'Sexo', 'Egreso']]
semana_egresos = pd.DataFrame(casos_positivos.groupby(['SEMANA','Egreso'])['Identificacion'].count()).reset_index()

semana_egresos_fallecidos = semana_egresos[semana_egresos['Egreso'] == 'Fallecido']
figura1 = px.line(semana_egresos_fallecidos, x = "SEMANA", y = "Identificacion", color = "Egreso")

edad_egresos = pd.DataFrame(casos_positivos.groupby(['Edad', 'Egreso'])['Identificacion'].count()).reset_index()
edad_egresos_fallecidos = edad_egresos[edad_egresos['Egreso'] == 'Fallecido']
figura2 = px.line(edad_egresos_fallecidos, x = "Edad", y = "Identificacion", color = "Egreso")

sexo_egresos = pd.DataFrame(casos_positivos.groupby(['Sexo', 'Egreso'])['Identificacion'].count()).reset_index()
sexo_egresos = pd.DataFrame(casos_positivos.groupby(['Sexo', 'Egreso'])['Identificacion'].count()).reset_index()
figura3 = px.bar(sexo_egresos, x = 'Sexo', y = "Identificacion", color ='Egreso')

card = dbc.Card(
    [
        dbc.CardImg(src="assets/images/map.png", top=True),
        dbc.CardBody(
            [
                html.H4("Geo espacial", className="card-title"),
                html.P(
                    "Informacion geo espacial de casos de Covid19 en Bucaramanga",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),

            ]
        ),
    ],
    style={"width": "18rem"},
)

work_equipe = dbc.CardGroup (
    [
        dbc.Card(
             [
        dbc.CardImg(src="/assets/images/ingeniero_sistemas.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Jimmy Pulido", className="card-title"),
                html.P(
                    "System Engineer of University National of Colombia "
                    "I like idioms and programming.",
                    className="card-text",
                ),
                dbc.Button("Profile", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
),

        dbc.Card(
            [
        dbc.CardImg(src="/assets/images/administrador.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Jhon Parra", className="card-title"),
                html.P(
                    "Business Administrator of University National of Colombia "
                    "I like series and animes.",
                    className="card-text",
                ),
                dbc.Button("Profile", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
),

        dbc.Card(

             [
        dbc.CardImg(src="/assets/images/matematico.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Fabian Pallares", className="card-title"),
                html.P(
                    "Mathematician of University National of Colombia "
                    "I like to be teacher.",
                    className="card-text",
                ),
                dbc.Button("Profile", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},


),

])


home = html.Div([
    html.H3('Covid-19 Bucaramanga Home'),

    ##card,
    dcc.Graph(figure = figura1, id= 'figura1'),
    dcc.Graph(figure = figura2, id= 'figura2'),
    dcc.Graph(figure = figura3, id= 'figura2'),
    work_equipe,



    dcc.Link('Go to App 2', href='/apps/app2')
])

layout2 = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
])