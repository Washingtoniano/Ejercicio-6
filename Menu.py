from Lista import lista
class menu:
    __li=lista()
    def __init__(self):
        self.__li=lista()
    def inicializar (self):
        self.opcion5()
        self.__li.agregar()
    def manejador(self,op):
        if (op)==1:
            self.opcion1()
        elif (op)==2:
            self.opcion2()
        elif (op)==3:
            self.opcion3()
        elif(op==4):
            self.opcion5()
        elif (op>5 or type(op)!=int):
            print ("Error")
    def opcion1(self):
        print("viajero con mayor cantidad de millas\n")
        self.__li.comparar()
    def opcion2(self):
        self.opcion5()
        num=int(input ("Ingrese el numero del viajero que desea agregar millas\n"))
        (self.__li.acumular(num))
    def opcion3(self):
        self.opcion5()
        num=int(input ("Ingrese el numero del viajero al que desea canjear millas\n"))
        self.__li.resta(num)
    def opcion5(self):
        self.__li.mostrarT()
