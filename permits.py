import pandas as pd

df = pd.read_csv("industrial-installations.csv")
df = df[df["Name"].str.contains("farm", case=False)]
df = df[df["Activity Type Description"].str.contains("intensive", case=False)]
df = df[df.columns.drop("Easting")]
df = df[df.columns.drop("Northing")]
df = df.sort_values(by=["Permission Date"], ascending=False)

df.to_csv("industrial-installations-n.csv", index=False)