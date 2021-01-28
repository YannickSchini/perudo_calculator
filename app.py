import dash_html_components as html
import dash_core_components as dcc
from server import app
from perudo_calculator import calculate_proba_graph_for_paco_faces
from perudo_calculator import description_card

dict_values = [str(x) for x in range(1, 26)]
dict_keys = range(1, 26)

app.layout = html.Div(
    id="app-container",
    children=[
        # Left column
        html.Div(id="left-column",
                 children=html.Div(children=[
                     description_card(),
                     dcc.Slider(id="Total Amount of Dices",
                                min=1,
                                max=25,
                                value=10,
                                step=None,
                                marks=dict(zip(dict_keys, dict_values)),
                                included=False)
                 ])),
        # Right column
        html.Div(id="right-column",
                 children=[dcc.Graph(id="Proba of matches")])
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
