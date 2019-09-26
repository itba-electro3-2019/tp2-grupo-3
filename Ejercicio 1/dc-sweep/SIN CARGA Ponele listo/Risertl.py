import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('RTL/1t0RTL.csv')
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
print("t-trans  Low to High= ",0.000503794-0.000503189)
print("t-Rise  Low to High= ",np.abs(0.000501321-0.00050337))
plt.show()
df = pd.read_csv('RTL/0t1RTL.csv')
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
print("t-trans  High to Low= ",4.93329e-7-4.06048e-7)
print("t-Rise  High to Low= ",5.28034e-7-4.51098e-7)
plt.show()





