import dash
import pandas as pd
import plotly.express as px
import dash_html_components as html
from plotly.graph_objects import Figure as Figure
from perudo_stats import get_proba_of_given_face
from server import app


@app.callback(dash.dependencies.Output("Proba of matches", "figure"),
              [dash.dependencies.Input("Total Amount of Dices", "value")])
def calculate_proba_graph_for_paco_faces(number_of_dice: int) -> Figure:
    """ Function used to calculate the probability of match graph based on \
        the total number of dice."""
    df = pd.DataFrame({"Number of matches": range(0, number_of_dice + 1)})
    df["Paco faces matches"] = df["Number of matches"].apply(
        lambda x: get_proba_of_given_face(number_of_dice, x, True))
    df["Normal faces matches"] = df["Number of matches"].apply(
        lambda x: get_proba_of_given_face(number_of_dice, x, False))
    fig = px.line(df,
                  x="Number of matches",
                  y=["Paco faces matches", "Normal faces matches"],
                  title="Probability of getting x matches")
    return fig


def description_card() -> html.Div:
    """ Generate the description card of the page.
    returns a Div containing the title & descriptions """
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
                use the statistics to the right to win !",
            ),
        ],
    )
