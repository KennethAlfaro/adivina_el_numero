import random as rd


class Juego:
    def __init__(self, num_intentos):
        self.intentos = num_intentos
        self.gano = False


    def get_numero(self,val_min,val_max):
        valor = int(input())
        while valor < val_min or valor > val_max:
            print("Entrada Incorrecta. Digite un valer {} y {}".format(val_min, val_max), end="")
            valor = int(input())
        return valor

    def menu(self):
        print("Bienvenido al juego de ADIVINE EL NUMERO ")
        print("Seleccione alguna de las siguentes opciones")
        print("   1.Jugador adivina el numero")
        print("   2. CPU adivina el numero")
        print("   3. Salir")
        print("             Digite una opcion: ", end="")
        opcion = self.get_numero(1,3)
        return opcion


    def get_aleatorio(self,val_min,val_max):
        return rd.randint(val_min,val_max)


    def run(self):
        while True:
            jugador = self.menu()
            if jugador == 1:
                cpu_num = self.get_aleatorio(1,100)
                while self.intentos > 0 :
                    print("¿Cual numero esto pensando? (0 - 100): ", end="")
                    valor = self.get_numero(1,100)
                    print(cpu_num)
                    if valor == cpu_num:
                        self.gano = True
                        self.intentos = 0
                    else:
                        if valor < cpu_num:
                            print("CPU dice: El numero es mayor que {}".format(valor))
                        elif valor > cpu_num:
                            print("CPU dice: El numero es menor que {}".format(valor))
                self.intentos -= 1

            elif jugador == 2:
                print("¿Cual numero desea que adivine el CPU? (0 - 100): ", end="")
                valor = self.get_numero((1, 100))
                lim_min = 0
                lim_max = 100
                while self.intentos > 0:
                    cpu_num = self.get_aleatorio(lim_min, lim_max)
                    if valor == cpu_num:
                        self.gano = True
                        self.intentos = 0
                    elif valor > cpu_num:
                        print("El numero {} es mayor ".format(cpu_num))
                        lim_max = cpu_num
                    elif valor > cpu_num:
                        print("El numero {} es menor ".format(cpu_num))
                        lim_min = cpu_num
                    self.intentos -= 1

            if self.gano is True:
                print("Felicidades. adivino el numero")
            else: print("Lo siento perdedor")
            self.intentos = 7
            if jugador == 3:
                break