import dask.dataframe as dd

df = dd.read_csv(r'data_cleaning\csv\data\air_traffic_data.csv')
print(df.head())