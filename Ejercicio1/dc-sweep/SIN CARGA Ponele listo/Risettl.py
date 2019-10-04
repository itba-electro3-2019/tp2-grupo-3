import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('TTL/1t0TTL.csv')
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
print("t-trans  Low to High= ",0.000502076-0.000501769)
print("t-Propagation  Low to High= ",np.abs(0.000501318-0.000501853))
plt.show()
df = pd.read_csv('TTL/0t1TTL.csv')
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
print("t-trans  High to Low= ",5.58713e-7-5.20347e-7)
print("t-Propagation  High to Low= ",5.46936e-7-5.45112e-7)
plt.show()





