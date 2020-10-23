import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64


## Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px

semana_egresos_fallecidos = pd.read_csv("Data/semana_egresos_fallecidos.csv")
edad_egresos_fallecidos = pd.read_csv("Data/edad_egresos_fallecidos.csv")
sexo_egresos = pd.read_csv("Data/sexo_egresos.csv")


figura1 = px.line(semana_egresos_fallecidos, x = "SEMANA", y = "Identificacion", color = "Egreso")
figura2 = px.line(edad_egresos_fallecidos, x = "Edad", y = "Identificacion", color = "Egreso")
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
        dbc.CardImg(src="/assets/images/profile.png", top=True),
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
        dbc.CardImg(src="/assets/images/profile.png", top=True),
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
        dbc.CardImg(src="/assets/images/profile.png", top=True),
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
    


    dcc.Link('Go to App 2', href='/apps/app2')
])

aboutus = html.Div([
    work_equipe,

])
