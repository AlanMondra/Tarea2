# %%
import pandas as pd
import seaborn as sns #para la visulazacion grafica
df = pd.read_csv('ulabox.csv')
# %%
# boxplots
df.corr()
sns.boxplot(data=df,x="customer",y="total_items",hue="weekday")

# %%
