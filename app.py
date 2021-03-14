import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Dataset Processing

df_emissions = pd.read_csv('emission_full.csv')
df = df.drop(6, errors='ignore')  # Drops the 'total sales' row



options = [{'label': 'Month of July', 'value': 'July'},
           {'label': 'Month of August', 'value': 'August'},
           {'label': 'Month of September', 'value': 'September'}]




@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='drop', component_property='value')]
)
def callback_1(input_value):
    data_bar = dict(type='bar',
                    y=df[input_value],
                    x=df['Product'],
                    texttemplate='<b>%{y} €</b>',
                    textposition='outside'
                    )

    layout_bar = dict(yaxis=dict(range=(0, 1500),
                                 title='Monetary Units'
                                 )
                      )

    return go.Figure(data=data_bar, layout=layout_bar)
# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1('Exercise 3 Data Visualization Example'),

    html.Br(),

    html.Label('Choose a Month:'),
    dcc.Dropdown(
        id='drop',
        options=options,
        value='July'
    ),

    dcc.Graph(
        id='example-graph'
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)

