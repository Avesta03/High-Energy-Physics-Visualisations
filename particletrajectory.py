import plotly.graph_objs as go
import pandas as pd

data = pd.read_csv('particledata.csv')

traces = [] # Trace for each particle
for particle in data.index:
    trace = go.Scatter3d(
        x=[data.loc[particle, 'x']],
        y=[data.loc[particle, 'y']],
        z=[data.loc[particle, 'z']],
        mode='lines',
        line=dict(
            color='blue',
            width=2
        )
    )
    traces.append(trace)

fig = go.Figure(data=traces) # Creating the fig

fig.update_layout( # Setting up the layout here
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z')
    ),
    title='Particle Trajectories'
)

fig.show()
