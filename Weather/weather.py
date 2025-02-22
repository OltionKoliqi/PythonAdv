import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv')


avg_temp_continent = df.groupby('Continent')['Average TEMP'].mean()

plt.figure(figsize=(10,6))


avg_temp_continent.plot(kind='line', marker='o', color='skyblue')

plt.title('Average Temp per Continent')
plt.xlabel('Continent')
plt.ylabel('Average Temp')

plt.show()