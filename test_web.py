import worldmap
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib

matplotlib.use('agg')

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Interactive Matplotlib with Dash", className='mb-2', style={'textAlign':'center'}),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='category',
                value='Number of Solar Plants',
                clearable=False,
                options=df.columns[1:])
        ], width=4)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph-matplotlib', figure={})
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            html.Img(id='map')
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dag.AgGrid(
                id='grid',
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                columnSize="sizeToFit",
            )
        ], width=12, md=6),
    ], className='mt-4'),
])

@app.callback(
    Output('bar-graph-matplotlib', 'figure'),
    Output('grid', 'defaultColDef'),
    Output(component_id="map", component_property="src"),
    Input('category', 'value'),
)
def plot_data(category_name):
    fig_bar_matplotlib = px.bar(df, x="State", y=category_name).update_xaxes(tickangle=330)

    my_cell_style = {
        "styleConditions": [
            {
                "condition": f"params.colDef.field == '{category_name}'",
                "style": {"backgroundColor": "#d3d3d3"},
            },
            {   "condition": f"params.colDef.field != '{category_name}'",
                "style": {"color": "black"}
            },
        ]
    }

    county_names = ['Norway', 'Nederland', 'brazile', 'austrialia']
    opacity = [10, 25, 35, 15]
    results = worldmap.plot(county_names, opacity=opacity, map_name='world', cmap='Set1')

    print("RESULTS = ", results)

    map_data = f"data:image/png;base64,"

    return fig_bar_matplotlib, {'cellStyle': my_cell_style}, map_data

app.run(debug=False, port=8000)
