import pandas as pd 
import matplotlib as mpl
import numpy as np

import plotly 
import plotly.graph_objects as go

df = pd.read_csv("ourDataset.csv")

agencyArr = (list(df))

fig = go.Figure(data=[go.Pie(labels=agencyArr[5:], 
                             values=df[agencyArr[5:]].sum()
                             )
                             ])

fig.show()

