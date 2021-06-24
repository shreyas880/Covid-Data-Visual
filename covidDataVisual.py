import pandas as pd
import plotly.express as pl

df = pd.read_csv('CovidData.csv')

graph = pl.line(df,x = 'date',y = 'cases',color = 'country',title = 'Covid cases')
graph.show()