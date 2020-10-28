import pandas as pd

df = pd.read_csv('ulabox_orders_with_categories_partials_2017.csv')

print("Tamaño del dataset:",df.shape)
df.info()
# df.describe()