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
                                html.H4("Risk of Death",
                                        className="card-title"),
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

    dbc.Row(

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
                                {"label": "Enfermedad Cardiaca",
                                 "value": 4},
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
                                {"label": "Insificiencia renal",
                                 "value": 8},
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

    dcc.Graph(figure=edad_mortalidad, id='edad_fallecidos'),


])


aboutus = html.Div([

    dbc.CardDeck([

        dbc.Card([

            html.Div([

                 dbc.CardImg(src="assets/images/profiles/Alejandro.jpeg",
                             top=True, className="img-circle"),
                 dbc.CardBody([
                     html.H4("Alejandro Ospina",
                             className="card-title m-a-0 m-b-xs"),
                     html.Div([
                         html.A([ 
                                html.I(className="fa fa-linkedin"),
                                html.I(className="fa fa-linkedin cyan-600"),
                                ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/alejandro-ospina-cortés-317125158/"),

                         html.A([
                             html.I(className="fa fa-envelope"),
                             html.I(className="fa fa-envelope red-600"),
                         ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:aospinacortes@gmail.com"),

                     ], className="block clearfix m-b"),
                     html.P(
                         "Mathematician, Analytics Analyst at Accenture",
                         className="text-muted",
                     ),

                 ]

                 ),

                 ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                 dbc.CardImg(src="/assets/images/profiles/Fabian_gamboa.jpeg",
                             top=True, className="img-circle"),
                 dbc.CardBody([
                     html.H4("Fabian Gamboa",
                             className="card-title m-a-0 m-b-xs"),
                     html.Div([
                         html.A([
                                html.I(className="fa fa-linkedin"),
                                html.I(className="fa fa-linkedin cyan-600"),
                                ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/fabian-gamboa-01900b155"),

                         html.A([
                             html.I(className="fa fa-envelope"),
                             html.I(className="fa fa-envelope red-600"),
                         ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:fagamboas@unal.edu.co"),

                     ], className="block clearfix m-b"),
                     html.P(
                         "Economist, Campaign's structure Analyst, Seguros Bolívar.",
                         className="text-muted",
                     ),

                 ]

                 ),

                 ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Fabian.jpeg",
                            top=True, className="img-circle"),
                dbc.CardBody([
                    html.H4("Fabian Pallares",
                            className="card-title m-a-0 m-b-xs"),
                    html.Div([
                        html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/fabian-pallares-jaimes-643118164/"),

                        html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:fabianpallares23@gmail.com"),

                    ], className="block clearfix m-b"),
                    html.P(
                        "Systems engineering student.  Emphasis on information and management systems",
                        className="text-muted",
                    ),

                ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Jhon.jpeg",
                            top=True, className="img-circle"),
                dbc.CardBody([
                    html.H4("Jhon Alexis Parra",
                             className="card-title m-a-0 m-b-xs"),
                    html.Div([
                        html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/jhon-alexis-parra-abril-0a935515a/"),

                        html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                        ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:jhalpaab@gmail.com"),

                    ], className="block clearfix m-b"),
                    html.P(
                        "Master in Business student,  Electronic engineer and Business Administrator.",
                        className="text-muted",
                    ),

                ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),




    ]),
    html.Br(),
    dbc.CardDeck([

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Jimmy.jpeg",
                            top=True, className="img-circle"),
                dbc.CardBody([
                 html.H4("Jimmy Pulido",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                          html.I(className="fa fa-linkedin"),
                          html.I(className="fa fa-linkedin cyan-600"),
                          ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/jimmy-pulido-arias-0639411b3/"),

                     html.A([
                         html.I(className="fa fa-envelope"),
                         html.I(className="fa fa-envelope red-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:jiapulidoar@gmail.com"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Computer System Engineering student.",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),



        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Luz.jpeg",
                            top=True, className="img-circle"),
                dbc.CardBody([
                 html.H4("Luz Dary Vanegas",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                            html.I(className="fa fa-linkedin"),
                            html.I(className="fa fa-linkedin cyan-600"),
                            ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/luz-dary-vanegas-penagos-a8517958"),

                     html.A([
                            html.I(className="fa fa-envelope"),
                            html.I(className="fa fa-envelope red-600"),
                            ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:luzdaryvanegaspenagos@gmail.com"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Economista, especialista en estadística, Fraud prevention lead en PayU",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

        dbc.Card([

            html.Div([

                dbc.CardImg(src="/assets/images/profiles/Wilmer.jpeg",
                            top=True, className="img-circle"),
                dbc.CardBody([
                 html.H4("Wilmer Pineda",
                         className="card-title m-a-0 m-b-xs"),
                 html.Div([
                     html.A([
                         html.I(className="fa fa-linkedin"),
                         html.I(className="fa fa-linkedin cyan-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="https://www.linkedin.com/in/wilmer-pineda-85ab7262"),

                     html.A([
                         html.I(className="fa fa-envelope"),
                         html.I(className="fa fa-envelope red-600"),
                     ], className="btn btn-icon btn-social rounded white btn-sm", href="mailto:wpinedar@unal.edu.co"),

                 ], className="block clearfix m-b"),
                 html.P(
                     "Mathematician, MSc in Mathematics, PhD (c) in Statistics. Professor at Universidad Santo Tomás . Data Scientist at the Superintendencia de Servicios Públicos.",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),

         dbc.Card([

            html.Div([

                dbc.CardImg(src="assets/images/bucaramanga.png",
                            top=True, ),
                dbc.CardBody([

                 html.P(
                     "Agradecimientos a la Alcadía de Bucaramanga.",
                     className="text-muted",
                 ),

                 ]

                ),

            ],
                className="opacity_1"
            ),


        ],
            className="text-center",

        ),




    ]),


])
