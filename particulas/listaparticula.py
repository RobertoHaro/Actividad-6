from .particula import Particula

class ListaParticulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, Particula:Particula):
        self.__particulas.append(Particula)

    def agregar_inicio(self, Particula:Particula):
        self.__particulas.insert(0,Particula)
    
    def mostrar(self):
        for Particula in self.__particulas:
            print(Particula)

    def __str__(self):
        return "".join(
            str(Particula) for Particula in self.__particulas
        )