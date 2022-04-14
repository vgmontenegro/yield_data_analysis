from functions import get_data_and_pack, make_hist, list_gpkg_files
import pandas as pd

# Get all gpkg files
path = 'C:/Users/Victorio/Documents/Python Scripts/analise_produtividade/C8'
files = list_gpkg_files(path)


# Pack all files in a single dataframe
df_pack = pd.DataFrame()

for file in files:
    get_data_and_pack(file, df_pack, values='N')
print('Packing was completed successfully!\n')

df_pack.to_excel('all_data.xlsx', index=False)


# Make histrograms and sotre in png file
make_hist(df_pack)


# End
print('\nProcessing completed!')