import pandas as pd
import matplotlib.pyplot as plt

planeta=['Mercurio','Venus','Tierra','Marte','Júpiter','Saturno','Urano','Neptuno','Plutón']
lugar=[1,2,3,4,5,6,7,8,9]
masa=[0.06,0.82,1.00,0.11,318,95.1,14.6,17.2,0.002]
datos = {'planeta':planeta,'lugar' : lugar,'masa':masa}
planetas_ss = pd.DataFrame(datos)
print(planetas_ss)

for etiqueta , filas in planetas_ss.iterrows():
    print(etiqueta)
    print(filas)



nombre=['Paco','Juan','Andrés','Natalia','Vanesa','Miriam','Juan']
color=['rojo','verde','amarillo','verde','verde','rojo','amarillo']
edad=[24,30,41,22,31,35,22]
altura=[182,170,169,183,178,172,164]
peso=[74.8,70.1,60.0,75.0,83.9,76.2,68.0]
puntuacion=[83,500,20,865,221,413,902]
datos = {'nombre':nombre,'color':color,'edad':edad,'altura':altura,'peso':peso}
registro = pd.DataFrame(datos)
print(registro)


plt.plot(registro.iloc[:,2])
plt.title('Edad')
plt.show()

plt.scatter(registro['edad'],registro['peso'])
plt.title('Edad vs Peso')
plt.show()


paises=['China','India','Estados Unidos','Indonesia','Brasil']
poblaciones=[1.36,1.29,0.33,0.26,0.2]
datos = {'paises':paises,'poblaciones':poblaciones}
poblacion = pd.DataFrame(datos)
poblacion.index=['CH','IN','USA','ID','BR']
print(poblacion)

for etiqueta, fila in poblacion.iterrows():
    print(etiqueta)
    print(fila)

for etiqueta, fila in poblacion.iterrows():
    print(etiqueta+':'+fila['paises'])

data = pd.read_csv('dataset1.csv',index_col=0)
print(data)


plt.hist(data.iloc[:,0])
plt.title('Distribucion del largo del sepalo en cm')
plt.show()


plt.hist(data.iloc[:,1])
plt.title('Distribucion del largo del sepalo en cm')
plt.show()


plt.scatter(data['PetalLengthCm'],data['PetalWidthCm'])
plt.title('Dimensiones de los petalos')
plt.show()


indices =data[data['PetalLengthCm'] >= 2.5].index
data.loc[indices,'Tamaño'] = 'Grande'
data.loc[indices,'Color'] = 'r'
indices =data[data['PetalLengthCm'] <= 2.5].index
data.loc[indices,'Tamaño'] = 'Pequeño'
data.loc[indices,'Color'] = 'b'

print(data)


plt.scatter(data['PetalLengthCm'],data['PetalWidthCm'],c = data.loc[:,'Color'])
plt.title('Dimensiones de petalos')
plt.show()