import os
import dash
import dash_core_components as dcc 
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash")
])

if __name__ == "__main__":
    # Get port and debug mode from environment variables
    port = os.environ.get('dash_port')
    debug = os.environ.get('dash_debug')=="True"
    app.run_server(debug=debug, host="0.0.0.0", port=port)