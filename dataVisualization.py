import pandas as pd 
import matplotlib as mpl
import numpy as np

import plotly 
import plotly.graph_objects as go

df = pd.read_csv("ourDataset.csv")





# fig = go.Figure(data=[go.Pie(
# )
# ])

agencyArr = list(df)


fig = go.Figure(data=[go.Pie(labels=agencyArr, 
                             values=df.sum())


print(agencyArr[3:])


# unique = np.unique(categoriesArr, return_counts=True)
# counts = np.unique(categoriesArr, return_counts=True)


