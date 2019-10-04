import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#df = pd.read_csv('mtl.csv')
#VIH =2.48
#VOH=4.99621503
#VIL=0.66661774
#VOL=0.15170335


df = pd.read_csv('rtl.csv')
VIH=0.84
VOH=4.9811
VIL=0.47872
VOL=0.278
#df = pd.read_csv('ttl.csv')
#VIH=0.62750643
#VOH=4.95
#VIL=0.49
#VOL=0.07276178

plt.title("RTL-MOS")

Vin = np.asarray(df['1'])
VinPAPI = pd.DataFrame(Vin).ewm(com=0.1).mean()
Vout = np.asarray(df['3'])
VoutPAPI = pd.DataFrame(Vout).ewm(com=0.1).mean()

#t= np.asarray(df['x-axis'])
#plt.plot(t,Vin,'r',label = 'Entrada' )
#plt.plot(t,Vout,'g',label = 'Salida' )
#plt.plot(Vin,Vout,'b',label = 'guardado')
####TTL
VinPAPI = np.asarray(VinPAPI) +55.46880E-03
VoutPAPI = np.asarray(VoutPAPI)+55.46880E-03
##############
####MTL
#VinPAPI = np.asarray(VinPAPI) +32.03130E-03
#VoutPAPI = np.asarray(VoutPAPI)+32.03130E-03

plt.plot(VinPAPI,VoutPAPI,'r')


plt.ylabel("Vout")
plt.xlabel("Vin")
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.grid(which='minor', linestyle=':', linewidth=0.1, color='black')
Vin = np.asarray(VinPAPI)
Vout = np.asarray(VoutPAPI)
#for i in range(len(Vin)-1):
#    if((np.abs(np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i])))) < 46) and (np.abs(np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i])))) > 44)):
#        print("Ángulo:",np.rad2deg(np.arctan((Vout[i+1]-Vout[i])/(Vin[i+1]-Vin[i]))))
#        print("VI:", Vin[i])
#        print ("VO:",Vout[i])
#puntos relevantes MOS:
#
#puntos relevantes TTL:
#
#puntos relevantes RTL:
plt.show()

NMH=np.abs(VIH-VOH)
NML=np.abs(VIL-VOL)

print("VIH=",VIH)
print("VOH=",VOH)
print("VIL=",VIL)
print("VOL=",VOL)
print("NMH=",NMH)
print("NML=",NML)











