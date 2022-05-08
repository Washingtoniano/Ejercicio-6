from Viajero import ViajeroFrecuente
import csv
class lista():
	__indice=[]
	def __init__ (self):
		self.__indice=[]
	def agregar(self):
		archivo=open("Prueba.csv","r")
		reader=csv.reader(archivo,delimiter=';')
		bandera=False
		for fila in reader:
			if bandera==False:
				bandera=True
			else:
				unviajero=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
				self.__indice.append(unviajero)
		archivo.close()
		return self.__indice


	def acumular(self,num):
		ban=False
		for viajero in self.__indice:
			if viajero.numero()==num:
				ban=True
				valor=float (input("Ingrese las millas a acumular\n"))
				viajero=viajero+valor
				print (viajero)
		if ban==False:
			print ("Error")

	def mostrarT(self):
		for unviajero in self.__indice:
			print (unviajero)
	def comparar(self):
		max=0
		for viajero in ((self.__indice)):
			for viajero2 in self.__indice:
				if (viajero>viajero2):
				 	max=viajero
				elif(viajero2>viajero):
					max=viajero2
		for viajero in ((self.__indice)):
			if (viajero==max):
				print(viajero)


	def resta(self,num):
		ban=False
		for viajero in self.__indice:
			if viajero.numero()==num:
				ban=True
				valor=float (input("Ingrese las millas a canjear\n"))
				viajero=viajero-valor
				print (viajero)
		if ban==False:
			print ("Error")



