# Astro Pi Proyect Space3 Team
# IES Granadilla de Abona
# 20/06/2021
# Objetive: Create a graph through a text file for Astro Pi's project

import numpy as np
import matplotlib.pyplot as plt

f1 = open('data02.txt', 'r')
f2 = open('data03.txt', 'w')
for line in f1:
    cadena = line.split (',')
    field1 = cadena [0]
    field2 = cadena [1]
    field3 = cadena [2]
    field4 = cadena [3]
    print (field2+','+field3+','+field4)
    f2.write (field2+','+field3+','+field4+'\n')
f1.close()
f2.close()

data_file = np.loadtxt ('data03.txt',delimiter=',')

sensors = data_file[:,0:3]
print (sensors)

#avgx = np.mean (sensors, axis=0)
#print (avgx)
#plt.plot (avgx,'yo')
plt.plot (sensors[:,0],'y')
plt.plot (sensors[:,1],'r')
plt.plot (sensors[:,2],'b')

plt.legend (['X','Y','Z'])
plt.xlabel ('Measures')
plt.ylabel('Values')
plt.show()
plt.savefig ('astropi_plot.png')