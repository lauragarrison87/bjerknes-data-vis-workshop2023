import altair as alt
from vega_datasets import data

counties = alt.topo_feature(data.us_10m.url, 'counties')
source = data.unemployment.url

# IDs are mapping to https://www.census.gov/library/reference/code-lists/ansi.html#cou STATEFP|COUNTYFP
chloro = alt.Chart(counties).mark_geoshape().encode(
    color='rate:Q',
    tooltip=[
        alt.Tooltip("id:N", title="County"),
        alt.Tooltip(
            "rate:Q", title="Rate"
        ),
    ]
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(source, 'id', ['rate'])
).project(
    type='albersUsa'
).properties(
    width=1000,
    height=800,
    title="Highest US Unemployment Rates (2009) in Only a Few Counties"
)

chloro.configure_title(fontSize=20, anchor="start").save(
    "chloro.html"
)

