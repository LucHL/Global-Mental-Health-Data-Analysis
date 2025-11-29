import base64
from io import BytesIO
import pandas as pd

from dash import Dash, html
import dash_bootstrap_components as dbc

from plot_gen.age_participation import get_age_participation
from plot_gen.average_table import get_average_table
from plot_gen.country_participation import get_country_participation
from plot_gen.gender_participation import get_gender_participation
from plot_gen.social_interaction_by_screen_time import get_social_interaction_by_screen_time
from plot_gen.stress_level_distrib_by_gender import get_stress_level_distrib_by_gender
from plot_gen.weekly_work_hours_by_stress_level import get_weekly_work_hours_by_stress_level
from plot_gen.stress_level_by_sleep_hours import get_stress_level_by_sleep_hours


def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    return "data:image/png;base64," + encoded

df = pd.read_csv("archive/Mental_Health_Dataset.csv")

get_average_table(df)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Interactive Matplotlib with Dash", className="mb-2", style={"textAlign":"center", "padding-bottom": "32px"}),

    dbc.Row([
        dbc.Col([
            html.Img(src=fig_to_base64(get_country_participation(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_gender_participation(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_age_participation(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_social_interaction_by_screen_time(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_weekly_work_hours_by_stress_level(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_stress_level_distrib_by_gender(df)))
        ]),
        dbc.Col([
            html.Img(src=fig_to_base64(get_stress_level_by_sleep_hours(df)))
        ])
    ])
])

app.run(debug=False, port=8000)
