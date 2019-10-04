import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#df = pd.read_csv('MOS/1t0MTL.csv')
df = pd.read_csv('MOS/monch_ctl1 - Copy.csv')

Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid()
print("t-trans  Low to High= ",0.000503057-0.000502148)
print("t-Propagation  Low to High= ",np.abs(0.00050133-0.00050266))
plt.show()
df = pd.read_csv('MOS/0t1MTL.csv')
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])
t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
plt.legend()
plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid()
print("t-trans  High to Low= ",-2.385e-7-4.95905e-7)
print("t-Propagation  High to Low= ",-5.43873e-7-2.56421e-8)
plt.show()





