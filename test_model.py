import joblib 
import numpy as np 
model = joblib.load('regression.joblib')

data = [[50, 2, 0], [90, 3, 1]] # liste de liste (sklearn peut faire des prédictions sur plusieurs données )

data2 = np.array([[66, 1, 0]])

result = model.predict(data)

print(result)

print(model.predict(data2))