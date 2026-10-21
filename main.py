
# 1.  laibraries data analisis  for project

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 2.  for loding the data (head for only top 5 rows)

df = pd.read_csv('data.csv')
# print(df.head())

#  3. for cheking columns 
 
print(df.columns.tolist())


# 4. Data Cleaning(srtip is for removing the spaces, lower for small letter.' ', '_'  = this means space changing to under score)


# 1. Numaric columns cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())

#  Removing Duplicates
df = df.drop_duplicates()

# changing price string to flot

df['price'] = df["price"].astype(str).str.replace(",","").astype(float)
print(df['price'])

# changing area string to integer
df['area'] = df["area"].astype(str).str.replace(",","").astype(int)
print(df['area'])

# changing rate_per_sqft string to integer
df['rate_per_sqft'] = df["rate_per_sqft"].astype(str).str.replace(",","").astype(int)
print(df['rate_per_sqft'])

# 2. categorical colmns cleaning

df['status'] = df['status'].str.strip().str.lower()

df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera' : True, 'not approved by rera' : False})
# print(df['rera_approval'])

df['flat_type'] = df['flat_type'].str.strip().str.lower()

df = df.drop_duplicates()
# print(df)
# print(df.info())


# Questions

# Question 1 : Which is the costlist flat in the dataset ?

# costliest_flat = df.loc[df['price'].idxmax()]
# print(costliest_flat)

# Question 2 : which locality has the highest average price?

# df.groupby('locality')['price'].mean().idxmax()
# highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
# print(f"The locality with the highest average price is {highest_avg_price_locality}.")

# Question 3 : Which locality has the hightest rate per sqare foot ?

# highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")

# Question 4 : Do ready to move  properties cost more than-under-construction properties ?

# ready_to_move_avg_price =df[df['status'] == 'ready to move']['price'].mean()
# under_construction_avg_price = df[df['status']=='under constuction']['price'].mean()

# if ready_to_move_avg_price > under_construction_avg_price:
#     print("Ready to move properties cost on average than under-construction properties.")
# else:
#     print("Under-construction properties cost more on average than ready-to-move properties.")

# Question 5 : DO RERA apporoved prperties command a price premium ?

# rera_approved_avg_price =df[df['rera_approval'] == True]['price'].mean()
# rera_not_approved_avg_price = df[df['rera_approval']== False]['price'].mean()

# if rera_approved_avg_price > rera_not_approved_avg_price:
    # print("RERA approved properties command price premium on ")
# else:  
    # print("RERA approved prperties do not command a price preamium.")

# Question 6 : How does area impat price?
# scatter plot diagram.

# sns.scatterplot(data=df, x='area', y='price')
# plt.show()

# .Question 7 : Which BHK configuration is most expensive based on sqft rate ?

# most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
# print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK")

# Question 8 : WHich property  type is the costliest ?

# most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
# print(f"The most expensive property type is {most_expensive_property_type} now.")

# Question 9 : Do certain builters price higher ?
# print(df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5))

# print("The top 5 Buiders that price higher are:",end="")
# top_5_builders =(
#      df.groupby("company_name")

#      ["rate_per_sqft"].mean()
#      .sort_values(ascending=False)
#      .head(5)
# )
# print(top_5_builders)
# Question 10 : Are larger homes more expensive per sqft ?

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.title('Area vs Rate per Sq Ft')
plt.xlabel('Area (sq ft)')
plt.ylabel('Rate per Sq Ft (₹)')
plt.savefig('area_vs_rate.png', dpi=150, bbox_inches='tight')
plt.show(block=True)