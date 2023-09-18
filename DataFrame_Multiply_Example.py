# Importing pandas package
import pandas as pd

# Creating a dictionary
d = {
    'Food':['Burger','Pizza','Noodles','Pasta'],
    'Actual_Price':[70,250,120,150],
    'After_discount':[66,240,113,140],
    'Sales':[13,24,43,65]
}

# Creating a dataframe
df = pd.DataFrame(d)

# Display Dataframe
print("DataFrame :\n",df,"\n")

# Multiply columns
result = df[["Actual_Price", "After_discount"]].multiply(df["Sales"], axis="index")

# Display result
print("Result:\n",result)