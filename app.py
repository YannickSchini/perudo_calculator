import dash_html_components as html
import dash_core_components as dcc
from server import app
from perudo_calculator import calculate_proba_graph_for_paco_faces
from perudo_calculator import description_card, input_card

app.layout = html.Div(
    id="app-container",
    children=[
        # Left column
        html.Div(
            id="left-column",
            children=html.Div(
                children=[description_card(), input_card()])),
        # Right column
        html.Div(id="right-column",
                 children=[dcc.Graph(id="Proba of matches")])
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
