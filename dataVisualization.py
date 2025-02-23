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


def requestsByAgencyInZone(latRange, longRange):
    filterd = df[
        (df['latRange'] == latRange) & 
        (df['longRange'] == longRange)
        ]


    fig = go.Figure(data=[go.Pie(labels=agencyArr[5:], 
                                values=filterd[agencyArr[5:]].sum()
                                )
                                ])
    fig.show()

print(type(df["latRange"][0]))

latRange = "[np.float64(43.031182899999926), np.float64(43.03315019999992)]"
longRange = "[np.float64(-76.16553000000008), np.float64(-76.16301200000008)]"


requestsByAgency()
requestsByAgencyInZone(latRange, longRange)