import altair as alt
from vega_datasets import data


source = data.gapminder_health_income()
print(source.head())

# vega-altair scatterplot
alt_title = alt.TitleParams(
    ["Richest and longest-lived countries", "include all but African region"],
    fontSize=16,
    anchor="start"
)

scatter_plot_log = (
    alt.Chart(source, title=alt_title)
    .mark_circle()
    .encode(
        alt.X("income:Q", scale=alt.Scale(type="log"), title="GDP Per Capita (log scale)", axis=alt.Axis(labelExpr='"$"+datum.value', grid=False)),  # logarithmic scale to spread out countries on lower end of x-scale and encode population into visualization
        alt.Y("health:Q", scale=alt.Scale(zero=False), title="Mortality (years)", axis=alt.Axis(grid=False)),
        size=alt.Size("population:Q", scale=alt.Scale(range=[30, 2000])),  # add size encoding, adjust range param of default
        color=alt.Color(
            "population:Q", legend=None,
            scale=alt.Scale(scheme="tealblues"),  # add color/opacity encoding to regions
        ),
        strokeOpacity=alt.value(1),
        tooltip=["country", "income", "health", "population"]  # add tooltips
    ).configure_view(stroke=None).configure_axisY(
    titleAngle=0,
    titleAlign="left",
    titleY=-15,
    titleX=-40
).interactive()  # add basic interactivity
)
scatter_plot_log.save("alt_scatterplot.html")
