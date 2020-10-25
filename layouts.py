import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64


## Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px

#CSVS

dia_fallecidos = pd.read_csv("Data/mortalidad_dia.csv")
semana_fallecidos = pd.read_csv("Data/mortalidad_semana.csv")
dia_positivos = pd.read_csv("Data/casos_positivos_dia.csv")
semana_positivos = pd.read_csv("Data/casos_positivos_semana.csv")
edad_egresos_fallecidos = pd.read_csv("Data/edad_egresos_fallecidos.csv")
sexo_egresos = pd.read_csv("Data/sexo_egresos.csv")


#Figuras
fig_dia_fallecidos = px.line(dia_fallecidos, x="dia", y="casos")
fig_dia_fallecidos_acu = px.line(dia_fallecidos, x="dia", y="casos_acumulado")

fig_semana_fallecidos = px.line(semana_fallecidos, x="semana", y="casos")
fig_semana_fallecidos_acu = px.line(semana_fallecidos, x="semana", y="casos_acumulado")

fig_dia_positivos = px.line(dia_positivos, x="dia", y="casos")
fig_dia_positivos_acu = px.line(dia_positivos, x="dia", y="casos_acumulado")

fig_semana_positivos = px.line(semana_positivos, x="semana", y="casos")
fig_semana_positivos_acu = px.line(semana_positivos, x="semana", y="casos_acumulado")



edad_mortalidad = px.line(edad_egresos_fallecidos, x = "Edad", y = "Identificacion", color = "Egreso")
figura3 = px.bar(sexo_egresos, x = 'Sexo', y = "Identificacion", color ='Egreso')




home = html.Div([

    html.H1('Covid-19 Bucaramanga Home'),

        
    dbc.Row(
            [
                dbc.Col([
                    dbc.Row(
                        html.H2("Positivos"),
                    ),
                    dbc.Row(
                        html.H4("15000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Recuperados"),
                    ),
                    dbc.Row(
                        html.H4("13000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Activos"),
                    ),
                    dbc.Row(
                        html.H4("1500"),
                    ),
                ]),
                
                dbc.Col([
                    dbc.Row(
                        html.H2("Fallecidos"),
                    ),
                    dbc.Row(
                        html.H4("500"),
                    ),
                ]),
            ]
        ),
        
    dbc.Col([

        dbc.Row([
            dbc.Col(
                    html.H3("Bucaramanga Global Situation"),
                    align="start"
            ),
            dbc.Col(


                    dbc.ButtonGroup([
                            dbc.Button("Change", id="change"),
                            dbc.Button("Accumulative", id="accumulative"),
                    ]),
            ), 

            dbc.Col(

                    dbc.ButtonGroup([
                            dbc.Button("Daily",id="daily"),
                            dbc.Button("Weekly", id="weekly"),
                    ]), 

            ),
        ]),

        ]),

        dbc.Row([
            dbc.Col(
                    html.Div("Positives"),
                    width=1
                    ),

            dbc.Col(
                    dcc.Graph(figure = fig_dia_fallecidos, id= 'positive_graphic'),

            ),


        ]),

        dbc.Row([

            dbc.Col(
                    html.H6("Deaths"),
                    width=1
                    ),

            dbc.Col(
                    dcc.Graph(figure = fig_dia_fallecidos_acu, id= 'death_graphic'),

            ),

            


        ]),
])


sir = html.Div([

    html.H1('Covid-19 Bucaramanga Home'),

        
    dbc.Row(
            [
                dbc.Col([
                    dbc.Row(
                        html.H2("Positivos"),
                    ),
                    dbc.Row(
                        html.H4("15000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Recuperados"),
                    ),
                    dbc.Row(
                        html.H4("13000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Activos"),
                    ),
                    dbc.Row(
                        html.H4("1500"),
                    ),
                ]),
                
                dbc.Col([
                    dbc.Row(
                        html.H2("Fallecidos"),
                    ),
                    dbc.Row(
                        html.H4("500"),
                    ),
                ]),
            ]
        ),



    html.H1("SIR MODEL"),

    
    html.P("SIR MODEL is a model can predict the numbers of infected people for COVID throught the time"),


  

  
])


risk = html.Div([

    html.H1('Covid-19 Bucaramanga Home'),

        
    dbc.Row(
            [
                dbc.Col([
                    dbc.Row(
                        html.H2("Positivos"),
                    ),
                    dbc.Row(
                        html.H4("15000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Recuperados"),
                    ),
                    dbc.Row(
                        html.H4("13000"),
                    ),
                ]),

                dbc.Col([
                    dbc.Row(
                        html.H2("Activos"),
                    ),
                    dbc.Row(
                        html.H4("1500"),
                    ),
                ]),
                
                dbc.Col([
                    dbc.Row(
                        html.H2("Fallecidos"),
                    ),
                    dbc.Row(
                        html.H4("500"),
                    ),
                ]),
            ]
        ),
    html.H1("Risk Of Death Predictor"),
    html.P("Model for predict the probability of death because of COVID-19"),

    dbc.Row (

        dbc.FormGroup(
                        [
                            dbc.Label("Age", html_for="slider"),
                            dcc.Slider(id="slider-age", min=0, max=100, step=1, value=50),
                        ]
                    ),

    ),

    
    dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup(
                                    [
                                        dbc.Label("Comorbilities"),
                                        dbc.Checklist(
                                        options=[
                                            {"label": "Asma", "value": 1},
                                            {"label": "Diabetes", "value": 2},
                                            {"label": "VIH", "value": 3},
                                            {"label": "Enfermedad Cardiaca", "value": 4},
                                        ],
                                        value=[],
                                        id="switches-input",
                                        switch=True,
                                    ),
                                    ]
                                ),
                     width=6, 
                     lg=3),

                dbc.Col(
                    dbc.FormGroup(
                                    [
                                        dbc.Label("Comorbilities"),
                                        dbc.Checklist(
                                        options=[
                                            {"label": "Cancer", "value": 5},
                                            {"label": "Obesidad", "value": 6},
                                            {"label": "Fumador", "value": 7},
                                            {"label": "Insificiencia renal", "value": 8},
                                        ],
                                        value=[],
                                        id="switches-input-2",
                                        switch=True,
                                    ),
                                    ]
                                ),
                     width=6, 
                     lg=3),



                dbc.Col([

                    dbc.Row(
                        html.Div("Prediction"), 
                        
                    ),

                    dbc.Row(
                        html.H4("Valor"),
                    ),               
                    
                               
                ]),
            ]
        ),

    dcc.Graph(figure = edad_mortalidad, id= 'edad_fallecidos'),


])



aboutus = html.Div([
    
    dbc.Row([
        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
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
                ),

        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Alejandro Ospina", className="card-title"),
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
                ),

        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Jimmy Pulido", className="card-title"),
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
        ),

    ]),


    dbc.Row([
        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Wilmer Pineda", className="card-title"),
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
                ),

        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Luz Vanegas", className="card-title"),
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
                ),

        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Fabian Gamboa", className="card-title"),
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
        ),

        dbc.Col(
             dbc.Card([
                        dbc.CardImg(src="/assets/images/profile.png", top=True),
                        dbc.CardBody([
                            html.H4("Jhon Parra", className="card-title"),
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
        ),

    ]),
   

])


