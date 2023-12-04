import altair as alt
import pandas as pd

source = pd.read_csv("../gapminder.csv")
source2014 = source.loc[source["Year"] == 2014]
sum_pop_2014 = source2014.groupby("Region")["Population"].sum().reset_index()
sum_pop_2014["Region"] = sum_pop_2014["Region"].str.capitalize()
sum_pop_2014["Percent"] = ((sum_pop_2014["Population"] / sum_pop_2014["Population"].sum()) * 100).map('{:,.1f}%'.format)
print(sum_pop_2014)

# set custom title for chart 
alt_title = alt.TitleParams(
    "Asian Regions Comprise Over 50% of Global Population (2014)",
    fontSize=16,
    anchor="start"
)

alt_pie = alt.Chart(sum_pop_2014, title=alt_title).mark_arc(outerRadius=100).encode(
    theta=alt.Theta("Population:Q").stack(True),  # this arranges text labels onto appropriate slices of the pie chart 
    color=alt.Color("Region:N", scale=alt.Scale(scheme="pastel1"), legend=None),
    tooltip=[
        alt.Tooltip("Region:N", title="Region"),
        alt.Tooltip(
            "Percent", title="Region Population"
        ),
    ]
)

slice_breaks = alt_pie.mark_arc(innerRadius=0, stroke="#fff")
text = alt_pie.mark_text(radius=115, size=12, fill="black").encode(text="Region")

alt.layer(alt_pie, slice_breaks, text).properties(width=600, height=600).save("alt_pie.html")
