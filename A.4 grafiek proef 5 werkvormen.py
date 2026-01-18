import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ===== 1. Data =====
data = {
    "Jaar": [2019, 2020, 2021, 2022, 2023],
    "Thuiswerken": [10, 55, 65, 60, 55],
    "Productiviteit_GenZ": [60, 66, 71, 74, 75],
    "Werkdruk_GenZ": [68, 64, 62, 59, 57],
    "Productiviteit_GenX": [58, 63, 68, 70, 72],
    "Werkdruk_GenX": [70, 68, 66, 64, 63]
}
df = pd.DataFrame(data)

# ===== 2. Subplots =====
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Generatie Z", "Generatie X"),
    shared_yaxes=False
)

# ===== 3. Kleurstijl =====
kleuren = {
    "productiviteit": "#e3cbb6",
    "werkdruk": "#f5e0ce",
    "thuiswerken": "#d1b69e"
}

# ===== 4. Gen Z =====
fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Thuiswerken"],
    mode="lines+markers",
    name="Thuiswerken",
    line=dict(color=kleuren["thuiswerken"], width=3, dash="dash"),
    marker=dict(size=10),
    hovertemplate=(
        "<b>Gen Z</b><br>"
        "Jaar: %{x}<br>"
        "Thuiswerken: %{y:.1f}%<extra></extra>"
    )
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Productiviteit_GenZ"],
    mode="lines+markers",
    name="Productiviteit (Gen Z)",
    line=dict(color=kleuren["productiviteit"], width=4),
    marker=dict(size=10),
    hovertemplate=(
        "<b>Gen Z</b><br>"
        "Jaar: %{x}<br>"
        "Productiviteit: %{y:.1f}%<extra></extra>"
    )
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Werkdruk_GenZ"],
    mode="lines+markers",
    name="Werkdruk (Gen Z)",
    line=dict(color=kleuren["werkdruk"], width=3, dash="dot"),
    marker=dict(size=10),
    hovertemplate=(
        "<b>Gen Z</b><br>"
        "Jaar: %{x}<br>"
        "Werkdruk: %{y:.1f}%<extra></extra>"
    )
), row=1, col=1)

# ===== 5. Gen X =====
fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Thuiswerken"],
    mode="lines+markers",
    name="Thuiswerken",
    line=dict(color=kleuren["thuiswerken"], width=3, dash="dash"),
    marker=dict(size=10),
    showlegend=False,
    hovertemplate=(
        "<b>Gen X</b><br>"
        "Jaar: %{x}<br>"
        "Thuiswerken: %{y:.1f}%<extra></extra>"
    )
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Productiviteit_GenX"],
    mode="lines+markers",
    name="Productiviteit (Gen X)",
    line=dict(color=kleuren["productiviteit"], width=4),
    marker=dict(size=10),
    hovertemplate=(
        "<b>Gen X</b><br>"
        "Jaar: %{x}<br>"
        "Productiviteit: %{y:.1f}%<extra></extra>"
    )
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=df["Jaar"], y=df["Werkdruk_GenX"],
    mode="lines+markers",
    name="Werkdruk (Gen X)",
    line=dict(color=kleuren["werkdruk"], width=3, dash="dot"),
    marker=dict(size=10),
    hovertemplate=(
        "<b>Gen X</b><br>"
        "Jaar: %{x}<br>"
        "Werkdruk: %{y:.1f}%<extra></extra>"
    )
), row=1, col=2)

# ===== 6. Layout =====
fig.update_layout(
    font=dict(family="Roboto", color="#5c4633"),
    plot_bgcolor="white",
    paper_bgcolor="white",
    width=1000,
    height=550,
    hoverlabel=dict(
        bgcolor="#f5e0ce",
        font_size=14,
        font_family="Roboto"
    ),
    showlegend=False  # ✅ legenda/variabelen onder de grafiek verbergen
)

# ===== 7. Y-assen links per grafiek =====
fig.update_yaxes(
    title_text="Percentage (%)",
    range=[0, 80],
    ticksuffix="%",
    side="left",
    showline=True,
    mirror=False,
    row=1, col=1
)
fig.update_yaxes(
    title_text="Percentage (%)",
    range=[0, 80],
    ticksuffix="%",
    side="left",
    showline=True,
    mirror=False,
    row=1, col=2
)

fig.update_xaxes(title_text="Jaar")

fig.show()
fig.write_html("thuiswerken_productiviteit_nolegend2.html", include_plotlyjs="cdn")
