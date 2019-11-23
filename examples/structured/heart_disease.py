import kaggledatasets as kd

heart_disease = kd.structured.HeartDiseaseUCI(download=True)

df = heart_disease.data_frame()
print(df.head())
print(df.tail())

dataset = heart_disease.load()
for batch, label in dataset.take(1):
	for key, value in batch.items():
		print("{:16s}: {}".format(key,value))
