import pandas as pd
import plotly.graph_objects as go
import base64
import random
import plotly.io as pio

# ---- Browserrenderer instellen ----
pio.renderers.default = 'browser'

# ---- Data inladen ----
df = pd.read_csv(r"C:\Users\rosan\Downloads\mentale_ondersteuning_generaties_clean.csv")

# ---- Afbeeldingen inlezen en encoden ----
def encode_image(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

kopje_img = encode_image(r"C:\Users\rosan\Downloads\koffiekopje.png")
boon_img = encode_image(r"C:\Users\rosan\Downloads\koffieboon.png")

boontjes_perc = 5     # 1 boontje = 5%
boon_spacing = 0.15   # verticale ruimte tussen boontjes
kopje_spacing = 1.5   # horizontale ruimte tussen generaties

# ---- Basis figure ----
fig = go.Figure()

hover_x, hover_y, hover_text = [], [], []

# ---- Kopjes + boontjes tekenen ----
for i, row in enumerate(df.itertuples()):
    generatie = row.Generatie
    perc = row.Percentage

    x = i * kopje_spacing
    n_boontjes = int(perc / boontjes_perc)

    # --- Koffiekopje ---
    fig.add_layout_image(dict(
        source=kopje_img,
        x=x, y=-0.3,
        xref="x", yref="y",
        sizex=0.4, sizey=0.4,
        xanchor="center", yanchor="middle",
        layer="above"
    ))

    # --- Generatie label onder het kopje ---
    fig.add_annotation(
        x=x, y=-0.55,
        text=generatie,
        showarrow=False,
        font=dict(size=14, color="black"),
        xanchor="center"
    )

    # --- Boontjes tekenen ---
    for j in range(n_boontjes):
        jitter = random.uniform(-0.1, 0.1)  # kleine horizontale variatie
        fig.add_layout_image(dict(
            source=boon_img,
            x=x + jitter,
            y=j * boon_spacing,
            xref="x", yref="y",
            sizex=0.15, sizey=0.15,
            xanchor="center", yanchor="middle",
            layer="above"
        ))

    # --- Hoverpositie berekenen ---
    if n_boontjes > 0:
        y_val = (n_boontjes - 1) * boon_spacing / 2
    else:
        y_val = 0

    # --- Hoverdata toevoegen ---
    hover_x.append(x)
    hover_y.append(y_val)
    hover_text.append(f"{generatie}: {perc:.1f}%")

# ---- Onzichtbare hoverlaag ----
fig.add_trace(go.Scatter(
    x=hover_x,
    y=hover_y,
    text=hover_text,
    mode="markers",
    marker=dict(size=60, color="rgba(0,0,0,0)"),
    hovertemplate="<b>%{text}</b><extra></extra>"
))

# ---- Layout instellen ----
fig.update_xaxes(visible=False, range=[-1, len(df) * kopje_spacing + 1])
fig.update_yaxes(visible=False, range=[-1, (df["Percentage"].max()/boontjes_perc) * boon_spacing + 1])

fig.update_layout(
    margin=dict(l=20, r=20, b=40),
    plot_bgcolor="white",
    hoverlabel=dict(
        bgcolor="#f5e0ce",  # jouw huisstijl
        font_size=14,
        font_family="Roboto",
        font_color="#3a2d22"
    )
)

# ---- Legenda met boontje ----


# ---- Browser openen ----
fig.show()
fig.write_html("Mentale_ondersteuning10.html", include_plotlyjs="cdn")
