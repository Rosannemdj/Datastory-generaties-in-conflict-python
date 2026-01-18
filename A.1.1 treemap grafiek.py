import plotly.express as px

# Data: oorzaken en hun relatieve percentages
data = {
    "Oorzaak": [
        "Prestatiedruk",
        "Social media & vergelijking",
        "Schuldenstress & sociale onzekerheid",
        "Curlingouders",
        "Openheid / hulp zoeken"
    ],
    "Percentage": [30, 25, 20, 15, 10]
}

# Bruine koffiekleuren
coffee_colors = [
    "#d7b899",  # latte
    "#c69c72",  # cappuccino
    "#a67c52",  # koffie
    "#8b5e3c",  # dark roast
    "#5c4033"   # espresso
]

# Plotly treemap
fig = px.treemap(
    data,
    path=["Oorzaak"],
    values="Percentage",
    color="Oorzaak",
    color_discrete_sequence=coffee_colors
)

# Titel en layout
fig.update_layout(
    title="Koffievlekken van Mentale Druk bij Gen Z",
    title_font_size=22,
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()
