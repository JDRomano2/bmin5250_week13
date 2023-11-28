import sys

import pandas as pd
import numpy as np
from scipy import stats

# Catch something from `stdin`:
my_stdin = sys.stdin.read()

# Parse the string into a dataframe
df = pd.DataFrame([x.split(' ') for x in my_stdin.split("\n")[:-1]])

# Add the column names
with open("./diabetes_colnames.csv") as fp:
    colnames = fp.read().strip().split(" ")
df.columns = colnames

# convert string columns to numeric
string_dtypes = df.columns[df.dtypes.eq('object')]
df[string_dtypes] = df[string_dtypes].apply(pd.to_numeric, errors='coerce')
    
# filter the dataframe to only contain adults (age >= 18)
df_adult = df.loc[df['age'] >= 18, :] 

# Return the output to stdout:
print(df_adult)