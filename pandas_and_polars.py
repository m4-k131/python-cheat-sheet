import pandas as pd
import polars as pl

csv_path = ""

df = pd.read_csv(csv_path)

reduced_columns_df = df[["column_a", "column_b"]]
filtered_df = df[df["column_a"] > 0.5]
filtered_df = df[df["column_a"].str.startswith("a")]


dfs = []
grouped_dfs = df.groupby(["column_a", "column_b"])
for (column_a, column_b), group_df in grouped_dfs:
    dfs.append(grouped_dfs)

concat_df = pd.concat(dfs, ignore_index=True)
unique_values = df["column_a"].unique().tolist()
print(unique_values)

df.to_csv(csv_path, index=False)
