import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash( __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    assets_external_path='./',
    suppress_callback_exceptions=  True
)


server = app.server


from layouts import home, aboutus, sir, risk

## Resources 
PLOTLY_LOGO = app.get_asset_url("images/bucaramanga.png")

## end resources

sidebar_header = dbc.Row(
    [
        dbc.Col(

            html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, className="img-fluid")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="#",

        ),
        ),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(255,255,255,.5)",
                    "border-color": "rgba(255,255,255,.1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="rigth",
        ),
    ]
)

sidebar = dbc.Navbar( [  html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be

        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/home", id="page-1-link"),
                    dbc.NavLink("SIR Model", href="/page-2", id="page-2-link"),
                    dbc.NavLink("Risk of death", href ="/page-3", id ="page-3-link"),
                    dbc.NavLink("About Us", href="/page-4", id="page-4-link"),
                ],
                vertical=True,
                navbar=True
            ),
            id="collapse",
        ),
    ],

),

],
color="dark",
    dark=True,
        id="sidebar",
)

content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
## fin Navbar


@app.callback(
    dash.dependencies.Output('slider-age-output', 'children'),
    [dash.dependencies.Input('slider-age', 'value'),
    dash.dependencies.Input('switches-input-comorbilities', 'value'),
    dash.dependencies.Input('switches-input-comorbilities-2', 'value'),
    dash.dependencies.Input('prediction-button', 'n_clicks')
    ])
def update_output(slider, switches, switches2, n_clicks):
    
    return 'You have selected {}, {}, {},{}'.format(slider,switches,switches2, n_clicks)



@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return  home
    elif pathname == "/page-2":
        return sir
    elif pathname == "/page-3":
        return risk
    elif pathname == "/page-4":
        return aboutus
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server( debug=True)




####Images etc 
