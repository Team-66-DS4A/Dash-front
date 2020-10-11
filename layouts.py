import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64

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

home = html.Div([
    html.H3('Covid-19 Bucaramanga Home'),

    card,

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