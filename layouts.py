import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
import dash_dangerously_set_inner_html


# Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px

# CSVS

dia_fallecidos = pd.read_csv("Data/mortalidad_dia.csv")
semana_fallecidos = pd.read_csv("Data/mortalidad_semana.csv")
dia_positivos = pd.read_csv("Data/casos_positivos_dia.csv")
semana_positivos = pd.read_csv("Data/casos_positivos_semana.csv")
edad_egresos_fallecidos = pd.read_csv("Data/edad_egresos_fallecidos.csv")
sexo_egresos = pd.read_csv("Data/sexo_egresos.csv")


# Figuras
fig_dia_fallecidos = px.line(dia_fallecidos, x="dia", y="casos")
fig_dia_fallecidos_acu = px.line(dia_fallecidos, x="dia", y="casos_acumulado")

fig_semana_fallecidos = px.line(semana_fallecidos, x="semana", y="casos")
fig_semana_fallecidos_acu = px.line(
    semana_fallecidos, x="semana", y="casos_acumulado")

fig_dia_positivos = px.line(dia_positivos, x="dia", y="casos")
fig_dia_positivos_acu = px.line(dia_positivos, x="dia", y="casos_acumulado")

fig_semana_positivos = px.line(semana_positivos, x="semana", y="casos")
fig_semana_positivos_acu = px.line(
    semana_positivos, x="semana", y="casos_acumulado")


edad_mortalidad = px.line(edad_egresos_fallecidos,
                          x="Edad", y="Identificacion", color="Egreso")
figura3 = px.bar(sexo_egresos, x='Sexo', y="Identificacion", color='Egreso')


#

home = dashboard = html.Div([
    dbc.Jumbotron(
        [
            html.Img(src="/assets/images/bga_rojo.png",
                     className="img-fluid")
        ], className="text-center"),

    dbc.Container(
        [

            dbc.CardGroup([
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="https://miro.medium.com/max/1400/1*9BrpVqQkpXGPP4fLcrk5Dw.gif", top=True),
                        dbc.CardBody(
                            [
                                html.H4("DasbBoard", className="card-title"),
                                html.P(
                                    "",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                    style={"width": "18rem"},
                ),
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="http://minjusticia.rt4apps.com/assets/images/s1.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("SIR Model", className="card-title"),
                                html.P(
                                    "",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                    style={"width": "18rem"},
                ),

                dbc.Card(
                    [
                        dbc.CardImg(
                            src="https://miro.medium.com/max/700/1*lsYP082Td5Ha0HzjmJfKBA.jpeg", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Risk of Death", className="card-title"),
                                html.P(
                                    "",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                    style={"width": "18rem"},
                )

            ])
        ]

    )

])

dashboard = html.Div([

    dbc.Row([
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("add_alert", className="material-icons"),
                                  className="float-right rounded w-40 danger text-center "),
                        html.H5(
                            "Positivos", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("15000"),
                    ],

                    className="pt-2 pb-2 box "
                ),
            ],
            style={"width": "18rem"},
        ),
        ],
            className="col-xs-12 col-sm-6 col-xl pl-1.5 pr-1.5 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [

                dbc.CardBody(
                    [html.Span(html.I("mood", className="material-icons"),
                               className="float-right rounded w-40 primary text-center "),
                        html.H5(
                            "Recuperados", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("13000"),

                     ],

                    className="pt-2 pb-2 box"
                ),
            ],
            style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl pl-1.5 pr-1.5 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("error", className="material-icons"),
                                  className="float-right rounded w-40 accent text-center "),
                        html.H5(
                            "Activos", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H3("1500", className="mt-0"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl pl-1.5 pr-1.5 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("local_hospital", className="material-icons"),
                                  className="float-right rounded w-40 warn text-center "),
                        html.H5(
                            "Fallecidos", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("500"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl pl-1.5 pr-1.5 pb-3 pb-xl-0"
        ),


    ],
        className="mt-1 mb-2"

    ),
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [

                                    dbc.ButtonGroup([
                                        dbc.Button("Daily", id="daily"),
                                        dbc.Button("Weekly", id="weekly"),
                                    ],
                                        className="float-right d-none d-lg-flex btn-group-sm btn-group"
                                    ),
                                    html.H5("Positive cases",
                                            className="card-title"),

                                    dcc.Graph(figure=fig_dia_fallecidos,
                                              id='positive_graphic'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-1.5 pr-1.5"
            ),
        ],
    ),

    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5("Deaths",
                                            className="card-title"),
                                    dcc.Graph(
                                        figure=fig_dia_fallecidos_acu, id='death_graphic'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-1.5 pr-1.5"
            ),
        ],
    ),

    dbc.Col([

        dbc.Row([
            dbc.Col(
                html.H3("Bucaramanga Global Situation",
                        className="text-muted font-weight-normal mt-2 mb-3 mr-5"),
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
                    dbc.Button("Daily", id="daily"),
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
                dcc.Graph(figure=fig_dia_fallecidos, id='positive_graphic'),

            ),


            ]),

    dbc.Row([

            dbc.Col(
                html.H6("Deaths"),
                width=1
            ),

            dbc.Col(
                dcc.Graph(figure=fig_dia_fallecidos_acu, id='death_graphic'),

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

    html.Div([
        html.Div([
            html.Span('COVID - 19 Bucaramanga - Risk Death Model'),


        ]),
    ]),




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
    
    
    dbc.Label("Age", html_for="slider"),


     html.Div([

             dcc.Slider(id="slider-age", min=0, max=100, step=1, value=5, 
             marks = {
                 0: '0',
                 10: '10',
                 20: '20',
                 30: '30',
                 40: '40',
                 50: '50',
                 60: '60',
                 70: '70',
                 80: '80',
                 90: '90',
                 100: '100'

             }
             ),
                         





        ]),

        
                
               




    dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup(
                                    [
                                        dbc.Label("Comorbilities"),
                                        dbc.Checklist(
                                        options=[
                                            {"label": "Asma", "value": 'ASM'},
                                            {"label": "Diabetes", "value": 'DIA'},
                                            {"label": "VIH", "value": 'VIH'},
                                            {"label": "Enfermedad Cardiaca", "value": 'EFC'},
                                        ],
                                        value=[],
                                        id="switches-input-comorbilities",
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
                                            {"label": "Cancer", "value": 'CAN'},
                                            {"label": "Obesidad", "value": 'OBS'},
                                            {"label": "Fumador", "value": 'FUM'},
                                            {"label": "Insificiencia renal", "value": 'IFR'},
                                        ],
                                        value=[],
                                        id="switches-input-comorbilities-2",
                                        switch=True,
                                    ),
                                    ]
                                ),
                     width=6, 
                     lg=3),



            dbc.Col([

                    dbc.Row(
                        html.Button('Predicted', id='prediction-button', n_clicks=0), 
                        
                    ),

                    dbc.Row(
                        html.Div(id='slider-age-output'), 
                    ),               
                    
                               
                ]),
            ]
        ),

    dcc.Graph(figure=edad_mortalidad, id='edad_fallecidos'),


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
