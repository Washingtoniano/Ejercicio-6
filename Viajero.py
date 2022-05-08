class ViajeroFrecuente():
    __numero = int
    __DNI = int
    __nombre = str
    __apellido = str
    __millasacum = float
    def __init__(self,numero=0,DNI=0,nombre="",apellido='',millasacum=0.0):
        self.__numero = numero
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacum = float(millasacum)
    def Millas(self):
        r=float(self.__millasacum)
        return (r)
    def numero (self):
        j=int (self.__numero)
        return (j)
    def __ge__(self, other):
        return (self.__millasacum>=other.__millasacum)
    def __gt__(self, other):
        return (self.__millasacum>other.__millasacum)
    def __lt__(self):
        return (self.__millasacum<other.__millasacum)
    def __le__(self, other):
        return (self.__millasacum<=other.__millasacum)
    def __add__(self, other):
        return (self.__millasacum+other)
    def __eq__(self, other):
       return (self.__millasacum==other.__millasacum)
    def __sub__(self, other):
        return(self.__millasacum-other)
    def __str__(self):
        return ("Numero:{}--DNI:{}--Nombre:{}--Apellido:{}--Millas:{}".format(self.__numero,self.__DNI,self.__nombre,self.__apellido,self.__millasacum))
