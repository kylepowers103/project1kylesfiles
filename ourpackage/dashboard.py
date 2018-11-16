import dash
import dash_core_components as dcc #will produce error here
import dash_html_components as html
from ourpackage import app  #db
from query import *
import plotly.graph_objs as go
from flask import render_template, jsonify, json

import pandas as pd #Delete?
from dash.dependencies import Input, Output

def country_goals():
    country= [x[0] for x in return_country_and_its_total_goals()]
    goals=[ x[1] for x in return_country_and_its_total_goals()]
    return [country,goals]

    # def return_country_and_its_total_goals(): using
    #     return session.query(Team.country, func.sum(Statistics.goals)).join(Statistics).group_by(Team.country).all()
#copy paste app.Layout













#
# data = [ #delete later
# #     {'name': "Brooklyn",
# #     'x': [0.86, 1.5, 2.2, 2.6, 2.7, 3, 3.67],
#     'y': [6.40, 8.34, 9.46, 11.13, 12.55, 18.68],
#     'type': "line"},
#     {'name': "Manhattan",
#     'x': [0.93, 1.33, 2.4, 2.6, 2.94, 3.34, 4.11],
#     'y': [9.34, 10.09, 13.24, 16.53, 15.64, 25.65],
#     'type': "line"}
# ]
#
# #uncomment and write the code for our Dash app below:
# app.layout = html.Div(children=[
#     html.H1("Check it out! This app has Flask AND Dash!"),
#     html.P("Adding some cool graph here soon:"),
#     dcc.Graph(
#         id = "uber_pricing_graph",
#         figure = {
#             'data': data,
#             'layout': {
#                 'title': 'Uber Pricing in Brooklyn and Manhattan'
#             }
#         }
#     )
# ])
