import altair as alt
import pandas as pd

garnes = pd.read_csv(
    "Garnes-2016-01-01-2019-09-16.csv", 
    index_col=0, # cols to use as row labels
    parse_dates=[0],  # parse first col as dates
    na_values="-9999",
    header=0, # explicitly pass this to replace existing header names
    names=["date", 
           "pressure", 
           "temp",
           "windspeed",
           "winddir",
           "humidity"])

temp = garnes.temp
groups = temp.groupby([temp.index.month, temp.index.hour]).mean()

d = []
for (month, hour),avgtemp in groups.items():
    d.append((month,hour,avgtemp))

df = pd.DataFrame(d, columns=("month", "hour", "avgtemp"))
print(df)


line = alt.Chart(df).mark_line().encode(
    alt.X("hour:O"),
    alt.Y("avgtemp:Q"),
    color=alt.Color("month:N")
)
line.save("temps.html")