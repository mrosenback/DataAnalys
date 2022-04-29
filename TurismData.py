import plotly
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

excel_file = 'Åland_turism_data.xlsx'
excel_file1 = 'epirapo.covid19case.fact_epirapo_covid19case.latest.xlsx'
df1 = pd.read_excel(excel_file, skiprows=2, nrows=46)
df2 = pd.read_excel(excel_file1, nrows=30)

turism = px.line(df1, x='År', y=['Finland', 'Sverige'], title='Inresande till Åland från Finland och Sverige mellan 1976 och 2021', labels={'variable': 'Land', 'value': 'Antal'})
coronafall = px.line(df2, x='Tid', y='Antal fall', title="Antalet covidfall på Åland under 2020")

turism.show()
coronafall.show()

fig = make_subplots(rows=1, cols=2)

df1.drop(df1.loc[0:38].index, inplace=True)
fig.add_trace(go.Scatter(x=df1['År'], y=df1['Totalt'], name='Turism'), row=1, col=1)
fig.add_trace(go.Scatter(x=df2['Tid'], y=df2['Antal fall'], name='Coronafall'), row=1, col=2)

fig.update_layout(height=700, title_text="Jämförelse på hur turismen påverkats av covid")
fig.update_xaxes(title_text="Tid")
fig.update_yaxes(title_text="Antal")

fig.show()