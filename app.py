import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Perudo Calculator"),
    html.Div(children="""
        This is a Perudo calculator: it's aim is to help you take the best \
        decisions and win at a game of Perudo !
    """)
])

if __name__ == "__main__":
    app.run_server(debug=True)
