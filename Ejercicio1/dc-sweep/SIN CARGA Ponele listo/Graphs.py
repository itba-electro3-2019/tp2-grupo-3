import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#df = pd.read_csv('mtl.csv')
df = pd.read_csv('mtl - Copy.csv')
#VIH =2.49454908
#VOH=4.88826341
#VIL=1.9478531
#VOL=0.07170335


#df = pd.read_csv('rtl.csv')
#VIH=0.86386726
#VOH=4.96033384
#VIL=0.45371101
#VOL=0.19103372

#df = pd.read_csv('ttl.csv')
VIH=0.59454747
VOH=4.96033384
VIL=0.41287307
VOL=0.03458998

plt.title("hola-MOS")

Vin = np.asarray(df['1'])
VinPAPI = pd.DataFrame(Vin).ewm(com=0.1).mean()
Vout = np.asarray(df['3'])--52.50000E-03
VoutPAPI = pd.DataFrame(Vout).ewm(com=0.1).mean()

t= np.asarray(df['x-axis'])
plt.plot(t,Vin,'r',label = 'Entrada' )
plt.plot(t,Vout,'g',label = 'Salida' )
#plt.plot(Vin,Vout,'b',label = 'guardado')
####TTL
#VinPAPI = np.asarray(VinPAPI)
#VoutPAPI = np.asarray(VoutPAPI)
##############
####MTL
VinPAPI = np.asarray(VinPAPI)
VoutPAPI = np.asarray(VoutPAPI)

#plt.plot(VinPAPI,VoutPAPI,'r')


plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
Vin = np.asarray(VinPAPI)
Vout = np.asarray(VoutPAPI)
for i in range(len(Vin)-1):
    if((np.abs(np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i])))) < 46) and (np.abs(np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i])))) > 44)):
        print("Ángulo:",np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i]))))
        print("VI:", Vin[i])
        print ("VO:",Vout[i])
#puntos relevantes MOS:
#
#puntos relevantes TTL:
#
#puntos relevantes RTL:

NMH=np.abs(VIH-VOH)
NML=np.abs(VIL-VOL)

print("VIH=",VIH)
print("VOH=",VOH)
print("VIL=",VIL)
print("VOL=",VOL)
print("NMH=",NMH)
print("NML=",NML)
plt.show()











