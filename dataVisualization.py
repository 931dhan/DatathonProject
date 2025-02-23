import pandas as pd 
import matplotlib as mpl
import numpy as np

import plotly 
import plotly.graph_objects as go

df = pd.read_csv("ourDataset.csv")
df2 = pd.read_csv("ourDatasetWithCategories.csv")

agencyArr = (list(df))

def requestsByAgency():
    fig = go.Figure(data=[go.Pie(labels=agencyArr[5:], 
                                values=df[agencyArr[5:]].sum()
                                )
                                ])
    fig.show()


# def requestsByAgencyInZone(latRange, longRange):
#     fig = go.Figure(data = )
