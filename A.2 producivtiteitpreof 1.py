import pandas as pd
import plotly.express as px

# CSV inlezen
df = pd.read_csv(r"C:\Users\rosan\Downloads\productiviteit_data_updated.csv")

# Berekeningen per generatie
resultaten = df.groupby("Generatie").agg(
    Gem_overuren=("Overuren", "mean"),
    Pct_hoog_bevlogen=("Bevlogenheid", lambda x: (x >= 4).mean() * 100),
    Pct_zeer_tevreden=("Tevredenheid", lambda x: (x == 5).mean() * 100)
).reset_index()

# Overuren omrekenen naar % van een 40-urige werkweek
resultaten["Pct_overuren"] = resultaten["Gem_overuren"] / 40 * 100

# Data in lang formaat
df_long = resultaten.melt(
    id_vars="Generatie",
    value_vars=["Pct_overuren", "Pct_hoog_bevlogen", "Pct_zeer_tevreden"],
    var_name="Indicator",
    value_name="Percentage"
)

# Labels leesbaarder maken
indicator_labels = {
    "Pct_overuren": "% extra werktijd (overuren)",
    "Pct_hoog_bevlogen": "% hoog bevlogen",
    "Pct_zeer_tevreden": "% zeer tevreden"
}
df_long["Indicator"] = df_long["Indicator"].map(indicator_labels)

# Kleurenpalet passend bij #f5e0ce
custom_colors = ["#8b5e3c", "#d7a46f", "#a6b88f"]

# Bar chart
fig = px.bar(
    df_long,
    x="Generatie",
    y="Percentage",
    color="Indicator",
    barmode="group",
    text_auto=".1f",
    title="Productiviteit per generatie: overuren, bevlogenheid en tevredenheid",
    color_discrete_sequence=custom_colors
)

# Layout
fig.update_layout(
    yaxis_title="Percentage (%)",
    plot_bgcolor="#f5e0ce",
    paper_bgcolor="#ffffff",
    title_font_size=20,
    legend_title="Indicator",
    margin=dict(t=50, l=40, r=40, b=40)
)

fig.show()