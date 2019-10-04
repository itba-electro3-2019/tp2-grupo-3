import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('TTL/1t0.csv')
plt.title("Rise-Time-RTL")
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid()
print("t-trans  Low to High= ",0.000501883-0.00050457)
print("t-Propagation  Low to High= ",np.abs(0.000501336-0.000502552))
plt.show()
df = pd.read_csv('TTL/0t1.csv')
plt.title("Rise-Time-RTL")
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid()
print("t-trans  High to Low= ",5.32187e-7-4.59066e-7)
print("t-Propagation  High to Low= ",5.26676e-7-4.93071e-7)
plt.show()





