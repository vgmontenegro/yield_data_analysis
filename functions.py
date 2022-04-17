import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os


def get_data_and_pack(path, df_pack, values='Massa_Prod'):
    gdf = gpd.read_file(path)
    data = gdf[values]
    title = path.split('.gpkg')[0]
    df_pack[title] = data
    print(f'{title} added to pack...')


def make_hist(df):
    print('Starting histogram production...')
    n = len(df.columns)
    lin = 3
    col = (n+(lin-1))//lin
    fig, axs = plt.subplots(lin, col, figsize=(20, 10))
    m = 0
    for i in range(lin):
        for j in range(col):
            if m < n:
                column = df.columns[m]
                m += 1
            else:
                break
            data = df[column]
            data = data[~np.isnan(data)]

            x_min = np.min(data)
            x_max = np.quantile(data, 0.75) + 2

            mu, std = norm.fit(data)
            x = np.linspace(0, 20, 500)
            y = norm.pdf(x, mu, std)

            title = column
            ax = axs[i, j]
            ax.hist(data, bins=1000, density=True, color='midnightblue', alpha=0.9)
            ax.plot(x, y, color='red')
            ax.set_xlim([x_min, x_max])
            ax.set_title(title)

            print('{}: Done'.format(title))

    plt.savefig('all_hist')
    print(f"All histograms was saved in the 'all_hist.png' file")


def list_gpkg_files(path):
    os.chdir(path)
    list = []
    for file in os.listdir():
        if file.endswith('.gpkg'):
            list.append(file)
    return list
