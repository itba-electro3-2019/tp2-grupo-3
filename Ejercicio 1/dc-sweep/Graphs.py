import numpy as np
import matplotlib.pyplot as plt


def not_num(content):
    if content == "0":
        return 0
    if content == "1":
        return 0
    if content == "2":
        return 0
    if content == "3":
        return 0
    if content == "4":
        return 0
    if content == "5":
        return 0
    if content == "6":
        return 0
    if content == "7":
        return 0
    if content == "8":
        return 0
    if content == "9":
        return 0
    if content == "-":
        return 0
    return 1

def read_file_spice(filename):
    file = open(filename,'r')
    lines = file.readlines()

    data = dict()

    data["Vf"] = []
    data["Vd"] = []
    data["Id"] = []
    print(lines)

    for i in range(1,len(lines)):
        pnt = 0
        c1 = ""
        c2 = ""
        c3 = ""
        while lines[i][pnt] != '\t':
            c1 += lines[i][pnt]
            pnt += 1

        while not_num(lines[i][pnt]):
            pnt += 1

        while lines[i][pnt] != '\t':
            c2 += lines[i][pnt]
            pnt += 1
        pnt += 1
        while not_num(lines[i][pnt]):
            pnt += 1
        while lines[i][pnt] != '\n':
            c3 += lines[i][pnt]
            pnt += 1

        c1 = float(c1)
        c2 = float(c2)
        c3 = float(c3)

        data["Vf"].append(c1)
        data["Vd"].append(c2)
        data["Id"].append(c3)

    return data

import pandas as pd
#df = pd.read_csv('MOS/mtl.csv')
df = pd.read_csv('RTL/rtl.csv')
#df = pd.read_csv('MOS/mtl.csv')

Vin = np.asarray(df['1'])
Vout = np.asarray(df['2'])
#t= np.asarray(df['x-axis'])
#plt.plot(t,Vin,'r',label = 'Entrada' )
#plt.plot(t,Vout,'g',label = 'Salida' )
plt.plot(Vin,Vout,'b',label = 'Ganancia')
plt.ylabel("Vout")
plt.xlabel("Vin")
legend = plt.legend()
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
for i in range(len(Vin)-1):
    print("Proporcionalidad:",np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i]))))
    print("Vin1 y 2:", Vin[i + 1], Vin[i])
#puntos relevantes MOS:
# Vin1 y 2: 2.66679692 2.57304692 45° de bajada
#Vin1 y 2: 2.09062505 1.99687505 de subida.
#puntos relevantes TTL:
#
#puntos relevantes RTL:
#
plt.show()











