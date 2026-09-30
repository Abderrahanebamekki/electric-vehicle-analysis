import pandas as pd

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
df = df.dropna(subset=["Electric Range"])

dim_vehicle = df[["VIN (1-10)", "Make", "Model", "Model Year", "Electric Vehicle Type"]].drop_duplicates().reset_index(drop=True)
dim_vehicle["vehicle_id"] = dim_vehicle.index + 1

dim_location = df[["County", "City"]].drop_duplicates().reset_index(drop=True)
dim_location = dim_location.drop_duplicates(subset=["City"]).reset_index(drop=True)
dim_location["location_id"] = dim_location.index + 1

df = df.merge(dim_vehicle, on=["VIN (1-10)", "Make", "Model", "Model Year", "Electric Vehicle Type"], how="left")
df = df.merge(dim_location, on=["County", "City"], how="left")

fact_table = df[["vehicle_id", "location_id", "Electric Range"]]

dim_vehicle.to_csv("dim_vehicle.csv", index=False)
dim_location.to_csv("dim_location.csv", index=False)
fact_table.to_csv("fact_table.csv", index=False)
