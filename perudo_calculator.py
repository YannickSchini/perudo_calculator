import dash
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from plotly.graph_objects import Figure as Figure
from perudo_stats import get_proba_of_given_face
from server import app


@app.callback(dash.dependencies.Output("Proba of matches", "figure"), [
    dash.dependencies.Input("Own Dice Number", "value"),
    dash.dependencies.Input("Other Players Dice Number", "value")
])
def calculate_proba_graph_for_paco_faces(other_dice_num: int,
                                         own_dice_num: int) -> Figure:
    """ Function used to calculate the probability of match graph based on \
        the total number of dice."""
    total_dice_num = own_dice_num + other_dice_num
    df = pd.DataFrame({"Number of matches": range(0, total_dice_num + 1)})
    df["Paco faces matches"] = df["Number of matches"].apply(
        lambda x: get_proba_of_given_face(total_dice_num, x, True))
    df["Normal faces matches"] = df["Number of matches"].apply(
        lambda x: get_proba_of_given_face(total_dice_num, x, False))
    fig = px.line(df,
                  x="Number of matches",
                  y=["Paco faces matches", "Normal faces matches"],
                  title="Probability of getting x matches")
    return fig


def description_card() -> html.Div:
    """ Generate the description card of the page.
    Returns a Div containing the title & descriptions """
    return html.Div(
        id="description-card",
        children=[
            html.H1("Perudo Calculator"),
            html.H3("Welcome to our Perudo helper page !"),
            html.Div(
                id="intro",
                children="Use statistics to help you make the best decisions \
                and win against your best friends and enemies at the \
                game of Perudo ! Input data about your game below, and\
                use the statistics to the right to win !")
        ])


def input_card() -> html.Div:
    """ Generation the inputs part of the page.
    Returns a Div containing all input setters. """
    dict_values = [str(x) for x in range(1, 26)]
    dict_keys = range(1, 26)
    return html.Div(
        id="inputs-card",
        children=[
            html.H5(children="How many dices do you have left ?"),
            dcc.Dropdown(id="Own Dice Number",
                         options=[{
                             "label": "One",
                             "value": 1
                         }, {
                             "label": "Two",
                             "value": 2
                         }, {
                             "label": "Three",
                             "value": 3
                         }, {
                             "label": "Four",
                             "value": 4
                         }, {
                             "label": "Five",
                             "value": 5
                         }, {
                             "label": "Six",
                             "value": 6
                         }],
                         placeholder="Select how many dices you have left",
                         value=0),
            html.H5(children="How many dices do other players have ?"),
            dcc.Slider(id="Other Players Dice Number",
                       min=1,
                       max=25,
                       value=10,
                       step=None,
                       marks=dict(zip(dict_keys, dict_values)),
                       included=False)
        ])
