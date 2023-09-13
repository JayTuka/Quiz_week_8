import matplotlib.pyplot as plt
import sqlite3
years =[]
co2 = []
temp = []
connection = sqlite3.connect(r".\climate.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM climatedata")
climateData = cursor.fetchall()
print(climateData)

for i in climateData:
    years.append(i[0])
    co2.append(i[1])
    temp.append(i[2])
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
plt.savefig("co2_temp_1.png")
