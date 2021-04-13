import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r"C:\Users\angel\Downloads\unemploymentdatacsv.csv")
print(df.head())
print(df.shape)
print(df.count)
for Year, row in df.iterrows():
    print(row["Women"])
if "Women" < "Men":
    print(True)
else:
    print(False)
if "Primary_School" < "High_School":
    print(True)
else:
    print(False)
if "Asian" < "Black":
    print(True)
else:
    print(False)
if "Professional_Degree" == "Associates_Degree":
    print (True)
elif "Professional_Degree" < "Associates_Degree":
    print((UnTrue))
else:
    print(False)
df['Person'] = df['Men'] + df['Women']
print(df)
df['POC'] = df['Black'] + df['Asian'] + df["Hispanic"]
print(df)
df_index = df.set_index("Year")
print(df_index)
df.sort_index()
print(df.fillna(0))
df_average_by_Year = df.groupby("Year")["Women"].mean()
print(df_average_by_Year)
df_average_by_Year.plot(kind="bar", title="Mean of Women")
plt.show()
