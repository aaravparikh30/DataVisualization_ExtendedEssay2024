import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_csv('nanodata.csv')
pd.set_option('display.max_columns', None)
df = df.round(decimals=2)

import seaborn as sns
import matplotlib.pyplot as plt

plt.matshow(df.corr())
plt.show()



print ('Heat Map Generation Complete')


from PIL import Image
im1 = Image.open("colorlegend.jpg")
im1.show()


import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()


print (df.corr())
print ('Console Data Compiled')

print (df)


