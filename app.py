import pandas as pd
import requests
import plotly.express as px
from dash import Dash, dcc, html

# URL dos dados abertos da CET-SP (substitua por uma URL real ou local)
url = "https://dadosabertos.cetsp.com.br/api/transito"  # Exemplo fictício

# Simulação de dados (caso não tenha acesso à API)
data = {
    "regiao": ["Leste", "Oeste", "Sul", "Norte", "Centro"],
    "congestionamento_km": [12.5, 8.3, 15.0, 5.2, 9.1],
    "data": ["2025-07-01"] * 5
}
df = pd.DataFrame(data)

# Criação do dashboard
app = Dash(__name__)
app.title = "Dashboard de Trânsito - CET-SP"

app.layout = html.Div([
    html.H1("Dashboard de Trânsito - Dados CET-SP", style={"textAlign": "center"}),

    dcc.Graph(
        id="grafico-congestionamento",
        figure=px.bar(df, x="regiao", y="congestionamento_km", color="regiao",
                      labels={"regiao": "Região", "congestionamento_km": "Km Congestionados"},
                      title="Congestionamento por Região")
    )
])

if __name__ == "__main__":
    app.run(debug=True)

