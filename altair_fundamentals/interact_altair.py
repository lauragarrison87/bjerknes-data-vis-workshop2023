import pandas as pd
import altair as alt

titanic = pd.read_csv("../../data/titanic.csv")
titanic.dropna(subset = ["Embarked"], inplace=True)
print(titanic.info())


# shneidermans mantra 
# overview first, zoom and filter, details on demand
# titanic: age against fare price 
# bar of embarkation 

selection = alt.selection_point(fields=["Pclass"], bind="legend")

age_fare = alt.Chart(titanic).mark_circle().encode(
    alt.X("Age:Q"),
    alt.Y("Fare:Q").scale(domain=[0,600]),
    color=alt.Color("Pclass:N"),
    opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)),
    tooltip=[
        alt.Tooltip("Name", title="Passenger Name"),
        alt.Tooltip("Age", title="Passenger Age"),
        alt.Tooltip("Fare", title="Paid"),
        ]
    ).add_params(
    selection
    ).properties(width=1000).interactive()

embark_highlight = alt.Chart(titanic).mark_bar().encode(
    alt.Y("Survived:N", title=None, axis=alt.Axis(labelAngle=0)),
    alt.X("count()").scale(domain=[0,800]),
    color="Pclass:N",
    opacity=alt.condition(selection, alt.value(0.8), alt.value(0.2)),
    row="Embarked"  
).add_params(selection).properties(width=400)


embark_filter = alt.Chart(titanic).mark_bar().encode(
    alt.Y("Survived:N", title=None, axis=alt.Axis(labelAngle=0)),
    alt.X("count()").scale(domain=[0,800]),
    color="Pclass:N",
    row="Embarked"  
).transform_filter(selection).properties(width=400)



alt.vconcat(age_fare, embark_filter).save("titanic_interactive.html")
