import dash
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
from perudo_stats import get_proba_of_given_face

app = dash.Dash(__name__)

df = pd.DataFrame({"Matches": range(1, 10)})
df["proba"] = df["Matches"].apply(lambda x: get_proba_of_given_face(10, x))

fig = px.line(df, x="Matches", y="proba")

app.layout = html.Div(children=[
    html.H1(children="Perudo Calculator"),
    html.Div(children="""
        This is a Perudo calculator: it's aim is to help you take the best \
        decisions and win at a game of Perudo !
    """),
    dcc.Graph(id='example-graph', figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
