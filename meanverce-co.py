import pandas as pd
df= pd.read_csv('titanic_cleaned.csv')
df.describe()

#Mean
mean_age = df['Age'].mean()
print("Mean Age : ", mean_age)

mean_fare = df['Fare'].mean()
print("Mean Fare : ", mean_fare)

#Variance
variance_age = df['Age'].var()
print("Variance Age : ", variance_age)

variance_fare = df['Fare'].var()
print("Variance Fare : ", variance_fare)

#Co-Variance
cov_matrix = df[['Age', 'Fare', 'Pclass']].cov()
cov_matrix

#Co-relation
corr_matrix = df[['Age', 'Fare', 'Pclass']].corr()
corr_matrix

# Grouped Statistics
df_new = df[['Survived', 'Age', 'Fare', 'Pclass']]
df_new.groupby('Survived').mean()