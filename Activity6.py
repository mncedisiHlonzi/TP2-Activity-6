#Step 1
import pandas as pd

df = pd.read_csv("C:\\Users\\mnced\\OneDrive\\Desktop\\tp test 1\\dataset - 2020-09-24.csv")

print(df.head())

print(df.tail())

print(df.head(3))

print(df.info())

print(df.describe())

#Step 2
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)
df = df.fillna(0)


#Step 3
duplicates = df.duplicated().sum()
print("Number of duplicate entries:", duplicates)
df = df.drop_duplicates()


#Step 4
print(df.dtypes)


#Step 4
print(df.columns)
print(df.size)
print(df.shape)


#Step 5
import matplotlib.pyplot as plt

# Scatter Plot
plt.scatter(df['Age'], df['Appearances'])
plt.title('Scatter Plot of Age vs. Appearances')
plt.xlabel('Age')
plt.ylabel('Appearances')
plt.show()

#Histogram
plt.hist(df['Appearances'], bins=5, color='blue', alpha=0.7)
plt.title('Histogram of Appearances')
plt.xlabel('Appearances')
plt.ylabel('Frequency')
plt.show()

#Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Club'], df['Appearances'], color='blue', alpha=0.7)
plt.title('Bar Chart of Club vs. Appearances')
plt.xlabel('Club')
plt.xticks(rotation=45)
plt.ylabel('Appearances')
plt.show()

#Box Plot
plt.figure(figsize=(6, 8))
plt.boxplot(df['Age'], vert=True, patch_artist=True, meanline=True, showmeans=True)
plt.title('Box Plot of Age')
plt.ylabel('Age')
plt.grid(True)
plt.show()