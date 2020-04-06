import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['month']).agg({'actual_max_temp':'sum', 'actual_min_temp': 'sum'}).reset_index()

data = [
    go.Scatter(x=new_df['month'],
               y=new_df['actual_min_temp'] / 30,
               mode='markers',
               marker=dict(size=new_df['actual_max_temp']/ 50, color=new_df['actual_max_temp'], showscale=True))
]
layout = go.Layout(title='Temperatures from July 2014 to June 2015', xaxis_title="Month",
                   yaxis_title="Min Temperatures", hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')