# %%
# PARTE 1
import pandas as pd
df = pd.read_csv('ulabox.csv')
# %%
# PARTE 2
del df['order'] #eliminamos order ya que no nos es relevante
print("Tamaño del dataset:",df.shape)
print("\nTIPO DE VARIABLE:\nCustumer = continuo\nTotal = continuo\nDiscount = discreto\nWeekDay = ordinal\nHour = discreto\nFood = discreto\nFresh = discreto\nDrinks = discreto\nHome = discreto\nBeauty = discreto\nHealth = discreto\nBaby = discreto\nPets = discreto\n")
# %%
# PARTE 3
print("\n--------Minimo--------")
print(df.min())
print("\n--------Maximo--------")
print(df.max())
# %%
# PARTE 4
# Medidas de tendencia central
print("\n----------------Medias-----------------")
print(df.mean())
print("\n----------------Medianas-----------------")
print(df.median())
print("\n----------------Moda-----------------")
print(df.mode())
# De dispersión
print("\n--------Desviacion Estandar---------")
print(df.std())
# Cuartiles
print("\n---------------------Cuartiles----------------------")
print(df.quantile([.25, .5, .75]))
