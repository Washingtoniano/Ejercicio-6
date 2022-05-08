from Menu import menu
from Lista import  lista
if __name__ == "__main__":
    unmenu=menu()
    unmenu.inicializar()

    op=int(input("Seleccione la opcion deseada\n\t1-Determinar viajero con mayor cantidad de millas\n\t2-Acumular Total de millas\n\t3-canjear Millas\n\t4-Mostrar Viajeros\n\t5-Salir\n"))
    while (op!=5):
        unmenu.manejador(op)
        op=int(input("Seleccione la opcion deseada\n\t1-Determinar viajero con mayor cantidad de millas\n\t2-Acumular Total de millas\n\t3-canjear Millas\n\t4-Mostrar Viajeros\n\t5-Salir\n"))


