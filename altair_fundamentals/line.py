import altair as alt
import pandas as pd

# bring in data
source = pd.read_csv("../gapminder.csv")
source["Year"] = pd.to_datetime(source["Year"], format="%Y")
source["Region"] = source["Region"].str.capitalize()
norway = source.loc[source["Country"] == "Norway"]
print(norway.head())

# vega-altair
alt.data_transformers.disable_max_rows()  # enable altair to load data >5000 rows

alt_title = alt.TitleParams(
    "Norwegian Population Steadily Increased Through 20th Century",
    fontSize=16,
    anchor="start"
)

alt_line = alt.Chart(norway, title=alt_title, width=400).mark_line().encode(
    alt.X("Year:T"),
    alt.Y("Population:Q", title="Population")#.scale(domain=(600000, 5500000))
).configure_axisY(titleAngle=0,titleAlign="left",titleY=-15,titleX=-70).configure_axis(grid=False).configure_view(
    stroke=None)
alt_line.save("alt_line.html")

# Split out regions to small multiples chart 
alt_title_region = alt.TitleParams(
    "Asian Region Population Spikes from 1960",
    fontSize=16,
    anchor="start"
)

alt_line_regions = alt.Chart(source, title=alt_title_region, width=200).mark_line().encode(
    alt.X("Year:T"),
    alt.Y("sum(Population):Q", title="Population"),
    color=alt.Color('Region:N', legend=None),  # do not need legend when having trellis chart (line below)
    column=alt.Column('Region:N', center=False),  # make trellis
    tooltip=[
        alt.Tooltip("Region:N"),
        alt.Tooltip(
            "sum(Population)", title="Region Population"
        ),
    ]
).configure_axisY(
    titleAngle=0,
    titleAlign="left",
    titleY=-15,
    titleX=-70
).configure_axis(grid=False).configure_view(
    stroke=None)
alt_line_regions.save("alt_line_regions.html")

