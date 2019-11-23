import kaggledatasets as kd

ny_airbnb = kd.structured.NewYorkAirbnbOpenData()

df = ny_airbnb.data_frame()
print(df.head())
print(df.tail())

dataset = ny_airbnb.load()
for batch in dataset.take(1):
	for key, value in batch.items():
		print("{:16s}: {}".format(key,value))
