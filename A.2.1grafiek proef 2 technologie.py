import pandas as pd
import plotly.express as px

# CSV-bestand laden (zorg dat het bestand in dezelfde map staat of pas pad aan)
df = pd.read_csv(r"C:\Users\rosan\Downloads\technologie_productiviteit.csv", comment='#')

# Data omzetten naar long format
df_long = df.melt(id_vars="Generatie", var_name="Indicator", value_name="Percentage")

# Definieer kleurenpalet passend bij #f5e0ce
custom_colors = ["#f5e0ce", "#e3cbb6", "#d1b69e"]

# Maak grouped bar chart
fig = px.bar(
    df_long,
    x="Generatie",
    y="Percentage",
    color="Indicator",
    barmode="group",
    labels={
        "Generatie": "Generatie",
        "Percentage": "Percentage (%)",
        "Indicator": "Indicator"
    },
    color_discrete_sequence=custom_colors
)

# Hovertemplate aanpassen: alleen percentage
fig.update_traces(
    hovertemplate="%{y:.1f}%<extra></extra>"
)

# Layout & hoverstijl
fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(size=14, color="#333"),
    showlegend=False,  # Legenda verbergen
    hoverlabel=dict(
        bgcolor="#f5e0ce",  # pastel achtergrondkleur
        font_size=14,
        font_family="Fredoka",
        font_color="#3a2d22"
    ),
    width=1000,   # 🔹 breedte in pixels
)

# Grafiek tonen
fig.show()

# Eventueel opslaan als HTML
fig.write_html("technologie_productiviteit_plot4.html", include_plotlyjs="cdn")
