import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Dados exemplo
df = px.data.gapminder().query("year == 2007")

# Criar app
app = dash.Dash(__name__)
server = app.server  # Necessário para o Render

fig = px.scatter(
    df, x="gdpPercap", y="lifeExp",
    size="pop", color="continent",
    hover_name="country", log_x=True,
    size_max=60
)

app.layout = html.Div([
    html.H1("Dashboard de Teste no Render"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
