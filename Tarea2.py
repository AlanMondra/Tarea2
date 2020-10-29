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
# %%
# PARTE 4
print("----------------Medias-----------------")
print(df.mean())
print("\n----------------Medianas-----------------")
print(df.median())
print("\n----------------Moda-----------------")
print(df.mode())
# print(df.describe())