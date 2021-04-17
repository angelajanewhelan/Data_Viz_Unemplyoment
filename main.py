import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(r"C:\Users\angel\Downloads\unemploymentdatacsv.csv")
print(df.head())
print(df.shape)
print(df.count)
plt.hist(df["Year"])
plt.show()
df_education = ["Primary_School", "High_School", "Associates_Degree"]
print(df_education)
df_education.append("Professional_Degree")
print(df_education)
df['Person'] = df['Men'] + df['Women']
print(df)
df['POC'] = df['Black'] + df['Asian'] + df["Hispanic"]
print(df)
round(df["Women"].mean())
round(df["Men"].mean())
round(df["Asian"].mean())
round(df["White"].mean())
round(df["Black"].mean())
round(df["Hispanic"].mean())
round(df["High_School"].mean())
round(df["Professional_Degree"].mean())
round(df["Primary_School"].mean())
round(df["Associates_Degree"].mean())
ave_women = 5
ave_men = 6
ave_asian = 5
ave_white = 5
ave_black = 11
ave_hispanic = 8
ave_High_School = 6
ave_Primary_School = 9
ave_Professional_Degree = 3
ave_Associates_Degree = 5

averages = [ave_women, ave_men, ave_asian, ave_white, ave_black, ave_hispanic, ave_High_School, ave_Primary_School, ave_Professional_Degree, ave_Associates_Degree]
print(averages)
print(averages.index(8))
np_averages = np.array(averages)
np_averages > 5
df_index = df.set_index("Year")
print(df_index)
df.sort_index()
print(df.fillna(0))
df_average_by_Year = df.groupby("Year")["Women"].mean()
print(df_average_by_Year)
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
df_average_by_Year_Women = df.groupby("Year")["Women"].mean()
print(df_average_by_Year_Women)
df_average_by_Year_Women.plot(kind="bar", title="Mean of Women")
plt.show()
df_average_by_Year_Men = df.groupby("Year")["Men"].mean()
print(df_average_by_Year_Men)
df_average_by_Year.plot(kind="bar", title="Mean of Men")
plt.show()
df_average_by_Year_Person = df.groupby("Year")["Person"].mean()
print(df_average_by_Year_Person)
df_average_by_Year_Person.plot(kind="bar", title="Mean of Person")
plt.show()
df_average_by_Year_Asian = df.groupby("Year")["Asian"].mean()
print(df_average_by_Year_Asian)
df_average_by_Year_Asian.plot(kind="bar", title="Mean of Asiann")
plt.show()
df_average_by_Year_Black = df.groupby("Year")["Black"].mean()
print(df_average_by_Year_Black)
df_average_by_Year_Black.plot(kind="bar", title="Mean of Black")
plt.show()
df_average_by_Year_Hispanic = df.groupby("Year")["Hispanic"].mean()
print(df_average_by_Year_Hispanic)
df_average_by_Year_Hispanic.plot(kind="bar", title="Mean of Hispanic")
plt.show()
df_average_by_Year_POC = df.groupby("Year")["POC"].mean()
print(df_average_by_Year_POC)
df_average_by_Year_POC.plot(kind="bar", title="Mean of POC")
plt.show()
df_average_by_Year_White = df.groupby("Year")["White"].mean()
print(df_average_by_Year_White)
df_average_by_Year_White.plot(kind="bar", title="Mean of White")
plt.show()
df_average_by_Year_Primary_School = df.groupby("Year")["Primary_School"].mean()
print(df_average_by_Year_Primary_School)
df_average_by_Year_Primary_School.plot(kind="bar", title="Mean of Primary_School")
plt.show()
df_average_by_Year_High_School = df.groupby("Year")["High_School"].mean()
print(df_average_by_Year_High_School)
df_average_by_Year_High_School.plot(kind="bar", title="Mean of High_School")
plt.show()
df_average_by_Year_Associates_Degree= df.groupby("Year")["Associates_Degree"].mean()
print(df_average_by_Year_Associates_Degree)
df_average_by_Year_Associates_Degree.plot(kind="bar", title="Mean of Associates_Degree")
plt.show()
df_average_by_Year_Professional_Degree = df.groupby("Year")["Professional_Degree"].mean()
print(df_average_by_Year_Professional_Degree)
df_average_by_Year_Professional_Degree.plot(kind="bar", title="Mean of Professional_Degree")
plt.show()

