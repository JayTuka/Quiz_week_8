import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

connection = sqlite3.connect(r".\climate.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM climatedata")


df = pd.DataFrame(cursor.fetchall(),  columns=['Year', 'CO2', 'Temperature'])
print(df)
years = df['Year'].tolist()
co2 = df['CO2'].tolist()
temp = df['Temperature'].tolist()
print(years)
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 


