import ctypes
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os
from tkinter import *

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def yield_histograms(path):
    gdf = gpd.read_file(path)
    data = gdf['N']
    data = data[~np.isnan(data)]
    title = path.split('.gpkg')[0]

    x_min = np.min(data)
    x_max = np.mean(data) + 3


    mu, std = norm.fit(data)
    x = np.linspace(0, 20, 500)
    y = norm.pdf(x, mu, std)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(data, bins=1000, density=True, color='midnightblue', alpha=0.9)
    ax.plot(x, y, color='red')
    ax.set_xlim([x_min, x_max])
    ax.set_title(title)
    plt.savefig(f'{title}_hist')

    print('{}:\n'
          '\tmu:  {}\n'
          '\tstd: {}'.format(title, mu, std))

path = 'C:/Users/Victorio/Documents/Python Scripts/analise_produtividade/C8'
os.chdir(path)

for file in os.listdir():
    if file.endswith('.gpkg'):
        yield_histograms(file)

Mbox('Code status', 'Success!', 1)


