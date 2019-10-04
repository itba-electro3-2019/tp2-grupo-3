import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('MOS/1t0.csv')
plt.title("Rise-Time-RTL-MOS")
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid()
print("t-trans  Low to High= ",0.000502232-0.000505063)
print("t-Propagation  Low to High= ",np.abs(0.000501342-0.000502994))
plt.show()
df = pd.read_csv('MOS/0t1.csv')
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
print("t-trans  High to Low= ",1.71032e-7-5.88221e-7)
print("t-Propagation  High to Low= ",-5.23439e-7-1.02291e-7)
plt.show()





