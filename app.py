import dash_html_components as html
import dash_core_components as dcc
from server import app
from perudo_calculator import calculate_proba_graph

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
