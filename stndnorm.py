import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv('titanic_cleaned.csv')
#df.head()
df = df[['Survived', 'Age', 'Fare', 'Pclass', 'SibSp', 'Parch']]
#df.head()
print("Original data statistics:")
print(df.describe())

scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print("After Min-Max Normalization:")
print(df.describe())

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print("After Standardization:")
print(df.describe())