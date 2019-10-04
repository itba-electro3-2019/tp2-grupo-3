import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('RTL/1t0.csv')
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
print("t-trans  Low to High= ",0.000503253-0.000505944)#de 0.1 a 0.9
print("t-Propagation  Low to High= ",np.abs(0.000501315-0.00050393))# PROPAGATION DE 0.5 a 0.5
plt.show()
df = pd.read_csv('RTL/0t1.csv')
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
print("t-trans  High to Low= ",-4.50002e-7--2.66185e-7)
print("t-Propagation  High to Low= ",5.26902e-7-2.66185e-7)
plt.show()





