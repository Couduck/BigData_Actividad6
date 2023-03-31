def ejercicio1():

    print("------------------------------------------------------\n")
    print("Ejercicio 1: Concatenar e imprimir mi nombre\n")
    print("------------------------------------------------------\n")
    input("PRESIONE ENTER PARA CONTINUAR...")

    nombre = "Patricio"
    apellido = "Estrada Carreto"
    nombreCompleto = nombre + " " + apellido

    print("\n------------------------------------------------------\n")
    print(nombreCompleto)
    print("\n------------------------------------------------------\n")
    input("PRESIONE ENTER PARA CONTINUAR...")

def ejercicio2():

    print("------------------------------------------------------\n")
    print("Ejercicio 2: Ingresar un numero del 1 al 100 e ingresar \n")
    print("------------------------------------------------------\n")
    input("PRESIONE ENTER PARA CONTINUAR...")

    valorCorrecto = False

    while valorCorrecto == False:

        try:

            print("------------------------------------------------------\n")
            numero = int(input("Ingrese un numero del 0 al 100: "))

            if(numero < 0 or numero > 100):
                print("------------------------------------------------------\n")
                print("ERROR: El valor es menor a 0 o mayor a 100, intentelo de nuevo.\n")
                print("------------------------------------------------------\n")
                input("PRESIONE ENTER PARA CONTINUAR...")

            else:
                print("\n------------------------------------------------------\n")

                valorCorrecto = True

                barraProgreso = "|"

                for i in range(0,numero):
                    barraProgreso += "#"

                diferencia = 100 - numero

                for i in range(0, diferencia):
                    barraProgreso += "-"

                barraProgreso += "|"

                print(f"Progreso: {numero}%\n\n{barraProgreso}")



        except ValueError:
            print("------------------------------------------------------\n")
            print("ERROR: El valor ingresado no puede convertirse a un numero entero, intentelo de nuevo.\n")
            print("------------------------------------------------------\n")
            input("PRESIONE ENTER PARA CONTINUAR...")


ejercicio1()
ejercicio2()
