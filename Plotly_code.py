import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/HarleyOwen/Xterm2019/master/2019-XTern-%20Work%20Sample%20Assessment%20Data%20Science-DS.csv')

fig = go.Figure(go.Scatter(x = df['xcoordinate'], y = df['ycoordinate'], mode='markers', marker_color = df['power_level'], text= df['power_level']))

fig.update_layout(title='Xtern 2019 scooter data',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True,)

fig.show()
