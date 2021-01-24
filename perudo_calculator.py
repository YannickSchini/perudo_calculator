import dash
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure as Figure
from perudo_stats import get_proba_of_given_face
from server import app


@app.callback(dash.dependencies.Output('Proba of matches', 'figure'),
              [dash.dependencies.Input('Total Amount of Dices', 'value')])
def calculate_proba_graph(number_of_dice: int) -> Figure:
    """ Function used to calculate the probability of match graph based on \
        the total number of dice."""
    df = pd.DataFrame({"Matches": range(1, number_of_dice)})
    df["proba"] = df["Matches"].apply(
        lambda x: get_proba_of_given_face(number_of_dice, x))
    fig = px.line(df, x="Matches", y="proba")
    return fig
