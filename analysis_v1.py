import pandas as pd
df = pd.read_csv('nanodata.csv')

import pandas_profiling as pp
pp.ProfileReport(df)

report = pp.ProfileReport(df)
report.to_file('profile_report.html')

from IPython import get_ipython
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
get_ipython().run_line_magic('inline')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np

plt.show(block=True)

def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist() }
    import plotly.graph_objects as go
    dfNew = df.corr()
    fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
    fig.show()

print ("Complete!")
