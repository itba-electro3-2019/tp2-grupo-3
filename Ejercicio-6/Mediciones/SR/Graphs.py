import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('../Dff/dff.csv')
#df = pd.read_csv('prop_s.csv')
Vin = np.asarray(df['1'])
Vout = np.asarray(df['3'])*10#--52.50000E-03


t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'b',label = 'Entrada' )
plt.plot(t,Vout,'y',label = 'Salida' )
plt.grid()
plt.legend()
plt.show()










