# %%
import pandas as pd
import seaborn as sns
df = pd.read_csv('ulabox.csv')
del df['order']
df.corr()
# %%
sns.heatmap(df.corr(),annot=True)
# %%
sns.boxplot(data=df,x="weekday",y="customer")

# %%
items = df[df["total_items"] < 29]
sns.boxplot(data=items,x="weekday",y="total_items")
# %%
disc = df[df["discount%"] > 0]
sns.boxplot(data=disc,x="weekday",y="discount%")
# %%
sns.boxplot(data=df,x="weekday",y="hour")
# %%
food = df[df["Food%"] > 0]
sns.boxplot(data=food,x="weekday",y="Food%")

# %%
fresh = df[df["Fresh%"] > 0] 
sns.boxplot(data=fresh,x="weekday",y="Fresh%")
#sns.scatterplot(data=fresh,x="weekday",y="Fresh%")
# %%
drinks = df[df["Drinks%"] > 0] 
sns.boxplot(data=drinks,x="weekday",y="Drinks%")

# %%
home = df[df["Home%"] > 0] 
sns.boxplot(data=home,x="weekday",y="Home%")
# %%
beauty = df[df["Beauty%"] > 0] 
sns.boxplot(data=beauty,x="weekday",y="Beauty%")
# %%
health = df[df["Health%"] > 0] 
sns.boxplot(data=health,x="weekday",y="Health%")
# %%
baby = df[df["Baby%"] > 0] 
sns.boxplot(data=baby,x="weekday",y="Baby%")
# %%
pets = df[df["Pets%"] > 0] 
sns.boxplot(data=pets,x="weekday",y="Pets%")
