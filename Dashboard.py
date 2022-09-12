# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selectio
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(
                                    id='site-dropdown',
                                    options = [
                                        {'label': 'ALL Sites', 'value': 'OPT1'},
                                        {'label': 'CCAFS LC-40', 'value': 'OPT2'},
                                        {'label': 'VAFB SLC-4E', 'value': 'OPT3'},
                                        {'label': 'KSC LC-39A', 'value': 'OPT4'},
                                        {'label': 'CCAFS SLC-40', 'value': 'OPT5'},
                                            ],
                                    placeholder = 'Select a launch site',
                                    searchable = True
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min = 0,
                                max = 10000,
                                step =1000,
                                value = [spacex_df['Payload Mass (kg)'].min(),spacex_df['Payload Mass (kg)'].max()]),
                                

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback( Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))


def generate_chart(names, values):

    fig = px.pie(spacex_df, names=site-dropdown, values ='class')
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output('success-payload-scatter-chart', 'figures'),
    [dash.dependencies.Input('site-dropdown', 'value')],
    [dash.dependencies.Input('payload-slider', 'value')])

def generate_chart(names, values):
    fig = px.scatter(spacex_df, x=payload-slider, y = 'class', color = site_dropdown)
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
