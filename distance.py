from scipy.spatial.distance import euclidean, cityblock, cosine
import pandas as pd
df = pd.read_csv('titanic_cleaned.csv')
#df_scaled = pd.read_csv('titanic_scaled.csv')

# Euclidean distance between two passengers
passenger1 = df.iloc[0][['Age', 'Fare','Pclass']].values
passenger2 = df.iloc[1][['Age', 'Fare','Pclass']].values

#passenger1_scaled = df_scaled.iloc[0][['Age', 'Fare', 'Pclass']].values
#passenger2_scaled = df_scaled.iloc[1][['Age', 'Fare', 'Pclass']].values

euclidean_distance = euclidean(passenger1, passenger2)
print("Euclidean Distance: ", euclidean_distance)

manhattan_distance = cityblock(passenger1, passenger2)
print("Manhattan Distance: ", manhattan_distance)

cosine_distance = cosine(passenger1, passenger2)
print("Cosine Distance: ", cosine_distance)