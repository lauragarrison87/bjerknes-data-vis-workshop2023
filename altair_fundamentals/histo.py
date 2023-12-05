import altair as alt
import pandas as pd

penguins_data = pd.read_json("../penguins.json")
print(penguins_data.head())

penguin_species_beak_depth_histo = (
    alt.Chart(penguins_data)
    .mark_bar(opacity=0.3, binSpacing=0)
    .encode(
        alt.X("Beak Depth (mm)", bin=True),
        alt.Y("count()").stack(None),
        alt.Color("Species:N"),
    )
    .properties(title="Penguin Beak Depth by Species")
)
penguin_species_beak_depth_histo.configure_title(fontSize=20, anchor="start").save(
    "histo.html"
)
