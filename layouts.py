import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
from app_ import app
from dash import callback_context as ctx

from dash.dependencies import Input, Output, State
# Data analytics library

import pandas as pd
import numpy as np
import plotly.express as px
import json

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


edad_mortalidad = px.bar(edad_egresos_fallecidos,
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
                                html.H3("Dashboard"),
                                html.P(
                                    "Here you can find graphs and data analysis about COVID-19 in Bucaramanga City",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Dashboard", color="primary", href="/page-5"),
                            ],
                            className="text-center"
                        ),
                    ],
                    style={"width": "18rem"},
                ),
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="https://i.pinimg.com/originals/e5/07/d7/e507d704d4b6fdcb17116762fcd99acd.gif", top=True),
                        dbc.CardBody(
                            [
                                html.H3("Spatial Model"),
                                html.P(
                                    "Spatial Model is a model can predict the numbers of infected people for COVID throught the time.",
                                    className="card-text",
                                ),
                                dbc.Button("Spatial Model",
                                           color="primary", href="/page-2"),
                            ],
                            className="text-center"
                        ),
                    ],
                    style={"width": "18rem"},
                ),

                dbc.Card(
                    [
                        dbc.CardImg(
                            src="https://wipitech.com/assets/images/ux.gif", top=True),
                        dbc.CardBody(
                            [html.H3("Risk of Death"),

                                html.P(
                                    "",
                                    className="card-text",
                            ),
                                dbc.Button("Risk Death Model", color="primary",
                                           href="/page-3", style={"align": "center"}),
                            ],
                            className="text-center"
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
            #style={"width": "18rem"},
        ),
        ],
            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
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
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("error", className="material-icons"),
                                  className="float-right rounded w-40 accent text-center "),
                        html.H5(
                            "Activos", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("1500"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
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
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
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
                                        dbc.Button(
                                            "Daily", id="pos_daily", className="btn btn-outline b-info  text-black"),
                                        dbc.Button(
                                            "Weekly", id="pos_weekly", className="btn btn-outline b-info  text-black"),
                                    ],
                                        className="float-right d-none d-lg-flex btn-group-sm btn-group",
                                        id="but_positive"
                                    ),

                                    dbc.Checklist(
                                        options=[
                                            {"label": "Cummulative", "value": 1},
                                        ],
                                        value=[],
                                        id="pos_cum",
                                        switch=True,
                                        className="md",
                                    ),


                                    html.H5("Positive cases",
                                            className="card-title"),

                                    dcc.Graph(
                                        id='positives'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
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
                                    dbc.ButtonGroup([
                                        dbc.Button(
                                            "Daily", id="death_daily", className="btn btn-outline b-info  text-black"),
                                        dbc.Button(
                                            "Weekly", id="death_weekly", className="btn btn-outline b-info  text-black"),
                                    ],
                                        className="float-right d-none d-lg-flex btn-group-sm btn-group"
                                    ),

                                    dbc.Checklist(
                                        options=[
                                            {"label": "Cummulative", "value": 1},
                                        ],
                                        value=[],
                                        id="death_cum",
                                        switch=True,
                                        className="md",
                                    ),
                                    html.H5("Deaths",
                                            className="card-title"),
                                    dcc.Graph(
                                        figure=fig_dia_fallecidos, id='death'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3"
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
                                    html.H5("Number of Covid-19 cases by age",
                                            className="card-title"),

                                    dcc.Graph(figure=edad_mortalidad,
                                              id='spatial_model_lines'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3", lg="6", sm="12", md="auto"
            ),

            dbc.Col(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5("State by sex",
                                            className="card-title"),

                                    dcc.Graph(figure=figura3,
                                              id='spatial_model_lines'),
                                ]
                            ),
                        ],
                    )
                ],
                className="mt-1 mb-2 pl-3 pr-3", lg="6", sm="12", md="auto"
            ),
        ],
    ),


],
    className='container',
)


risk = html.Div([

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
            #style={"width": "18rem"},
        ),
        ],
            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
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
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),
        dbc.Col([dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.Span(html.I("error", className="material-icons"),
                                  className="float-right rounded w-40 accent text-center "),
                        html.H5(
                            "Activos", className="card-title text-muted font-weight-normal mt-2 mb-3 mr-5"),
                        html.H4("1500"),
                    ],

                    className="pt-2 pb-2 box"
                ),
            ],
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
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
            #style={"width": "18rem"},
        ),
        ],

            className="col-xs-12 col-sm-6 col-xl-3 pl-3 pr-3 pb-3 pb-xl-0"
        ),


    ],
        className="mt-1 mb-2"

    ),


    dbc.Card(

        dbc.CardBody([
            html.H1("Risk Of Death Predictor"),
            dbc.Alert(
                "Select comorbilities and age for calculated risk of death by COVID-19",
                id="alert-prediction-death",
                dismissable=False,
                fade=False,
                is_open=True,
            ),
        ],
        ),
    ),

    dbc.Card(

        dbc.CardBody([

            dbc.Label("Age ", html_for="slider"),

            html.I(className="fa fa-question-circle",
                   id="tooltip-target-age",
                   style={"padding": "1rem"}, ),





            html.Div([

                dcc.Slider(id="slider-age", min=0, max=100, step=1, value=5,
                           marks={
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
            ]
            ),


        ],
        ),

    ),

    #dbc.Button("?", )

    dbc.Tooltip(
        "Select your age with the slider",
        target="tooltip-target-age",
    ),

    dbc.Tooltip(
        "Select the cormobilites that you have",
        target="tooltip-target-comorbidities",
    ),



    dbc.Row(
        [
            dbc.Col(

                dbc.Card(

                    dbc.CardBody([
                        dbc.FormGroup(
                            [
                                dbc.Label("Comorbidities"),
                                html.I(className="fa fa-question-circle",
                                       id="tooltip-target-comorbidities",
                                       style={"padding": "1rem"}, ),
                                dbc.Checklist(
                                    options=[
                                        {"label": "Diabetes",
                                         "value": 'DIA'},
                                        {"label": "Heart disease",
                                         "value": 'EFC'},
                                        {"label": "Cancer",
                                         "value": 'CAN'},
                                        {"label": "Obesity",
                                         "value": 'OBS'},
                                        {"label": "Renal insufficiency",
                                         "value": 'IFR'},
                                    ],
                                    value=[],
                                    id="switches-input-comorbidities",
                                    switch=True,
                                ),


                            ]
                        ),
                    ],
                    ),
                    color="primary",
                    outline=True,
                    style={"margin": "0.25rem auto 1.5rem"}
                ),


                width=3,
                lg=3),




            dbc.Col([

                    dbc.Card(
                        dbc.CardBody([

                            html.H4("Risk prediction of Death",
                                    className="card-prediciton-title"),
                            html.Div(id='slider-age-output'),
                            dbc.Progress("25%", value=25),


                        ]),

                        color="primary",
                        outline=True,
                        style={"margin": "0.25rem auto 1.5rem"},


                    ),





                    ],
                    width=6,
                    lg=6,


                    ),


            dbc.Col(

                dbc.Card(
                    dbc.CardBody([

                        html.H4("Risk classification",
                                className="card-classification-title"),

                        dbc.Alert(
                            "71-100% : High Risk\n"
                            "41-70% : Medium Risk\n"
                            "0-40% : Low Risk",
                            id="alert-prediction-risk",
                            dismissable=False,
                            fade=False,
                            is_open=True,
                        ),


                    ]),

                    color="primary",
                    outline=True,
                    style={"margin": "0.25rem auto 1.5rem"},


                ),
                width=3,
                lg=3,


            ),



        ]
    ),


    dbc.Row([

        dbc.Card(

            dbc.CardBody([


                dbc.Col(

                    dbc.Card(

                        dbc.CardBody(

                            dcc.Graph(figure=edad_mortalidad,
                                      id='edad_fallecidos'),

                        ),

                    ),

                ),


                dbc.Col(

                    dbc.Card(

                        dbc.CardBody(

                            dcc.Graph(figure=edad_mortalidad,
                                      id='edad_fallecidos'),

                        ),

                    ),

                ),






            ]),



        ),







    ]),


],
    className='container',
)


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

                 dbc.CardImg(src="assets/images/bucaramanga_logo.png",
                             top=True, className="img-fluid w-50 text-center"),
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


@app.callback(
    Output('positives', 'figure'),
    [Input('pos_daily', 'n_clicks'),
     Input('pos_weekly', 'n_clicks'), Input('pos_cum', 'value')])
def update_posfig(pos_daily, pos_weekly, pos_cum):
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if(len(pos_cum) == 1):
        if(button_id == "pos_daily"):
            return fig_dia_positivos_acu
        elif(button_id == "pos_weekly"):
            return fig_semana_positivos_acu
        return fig_dia_positivos_acu

    if(button_id == "pos_daily"):
        return fig_dia_positivos
    elif(button_id == "pos_weekly"):
        return fig_semana_positivos

    return fig_dia_positivos



@app.callback(
    Output('death', 'figure'),
    [Input('death_daily', 'n_clicks'),
     Input('death_weekly', 'n_clicks'), Input('death_cum', 'value')])
def update_deathfig(pos_daily, pos_weekly, pos_cum):
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if(len(pos_cum) == 1):
        if(button_id == "death_daily"):
            return fig_dia_fallecidos_acu
        elif(button_id == "death_weekly"):
            return fig_semana_fallecidos_acu
        return fig_dia_fallecidos_acu

    if(button_id == "death_daily"):
        return fig_dia_fallecidos
    elif(button_id == "death_weekly"):
        return fig_semana_fallecidos

    return fig_dia_fallecidos