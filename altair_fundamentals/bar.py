import altair as alt
import pandas as pd

# bring in data
source = pd.read_csv("../gapminder.csv")
source["Region"] = source["Region"].str.capitalize()
source2014 = source.loc[source["Year"] == 2014]
print(source2014.head())


alt_title = alt.TitleParams(
    "Europeans Earn Highest Average Income in 2014",
    fontSize=16,  # set different font size than default
    anchor="start"  # left align text of title on canvas
)

alt_bar = alt.Chart(source2014, title=alt_title, width=400).mark_bar().encode(
    alt.X("Region:N", sort="y", axis=alt.Axis(labelAngle=0)),
    alt.Y("mean(Income):Q", title="Average Annual Income($)")
)

# Error bars showing standard error is the default error bar in this API 
# https://altair-viz.github.io/user_guide/marks/errorbar.html
alt_error = alt.Chart(source2014).mark_errorbar().encode(
    alt.Y("Income:Q"), 
    alt.X("Region:N")
)

# layer together bar and error charts to a single plot, and 
# configure the y-axis label position at top left of chart, horizontal orientation
alt.layer(alt_bar, alt_error).configure_axisY(
    titleAngle=0,
    titleAlign="left",
    titleY=-15,
    titleX=-40
).save("alt_bar_err.html")
