import dash
import dash_html_components as html
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure as Figure
import dash_core_components as dcc
from perudo_stats import get_proba_of_given_face

app = dash.Dash(__name__)


@app.callback(dash.dependencies.Output('example-graph', 'figure'),
              [dash.dependencies.Input('Total Amount of Dices', 'value')])
def calculate_proba_graph(number_of_dice: int) -> Figure:
    """ Function used to calculate the probability of match graph based on \
        the total number of dice."""
    df = pd.DataFrame({"Matches": range(1, number_of_dice)})
    df["proba"] = df["Matches"].apply(
        lambda x: get_proba_of_given_face(number_of_dice, x))
    fig = px.line(df, x="Matches", y="proba")
    return fig


dict_values = [str(x) for x in range(1, 26)]
dict_keys = range(1, 26)

app.layout = html.Div(children=[
    html.H1(children="Perudo Calculator"),
    html.Div(children="""
        This is a Perudo calculator: it's aim is to help you take the best \
        decisions and win at a game of Perudo !
    """),
    dcc.Slider(id='Total Amount of Dices',
               min=1,
               max=25,
               value=10,
               step=None,
               marks=dict(zip(dict_keys, dict_values)),
               included=False),
    dcc.Graph(id='example-graph')
])

if __name__ == "__main__":
    app.run_server(debug=True)
