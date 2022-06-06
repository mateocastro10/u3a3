import numpy as np
from datetime import timedelta, datetime
import csv
from equipo import Equipo
class ManejaEquipo:
    __dimension=10
    __cantidad=0
    __incremento=2
    def __init__(self):
        self.__equipos=np.empty(self.__dimension,dtype=Equipo)
    def agregar(self,equipo):
        if(self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__equipos.resize(self.__dimension)
            self.__equipos[self.__cantidad]=equipo
            self.__cantidad+=1
        else:
            self.__equipos[self.__cantidad]=equipo
            self.__cantidad+=1
    def LeerArchivo(self):
        band=True
        archivo=open("equipos.csv")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(band):
                band=False
            else:
                equipo1=Equipo(fila[0],fila[1])
                self.agregar(equipo1)
        archivo.close()
    def mostrarEquipos(self):
        print('----------------Equipos----------------')
        for i in self.__equipos:
            print(i.getNombre())
    def Buscar(self,equipo):
        i=0
        retorna=None
        while(i<len(self.__equipos) and equipo!=self.__equipos[i].getNombre()):
            i+=1
        if(i<len(self.__equipos)):
            retorna=self.__equipos[i]
        else:print('Equipo no econtrado!')
        return retorna
    def ConsultarContratos(self):
        id=input('Ingrese nombre del equipo:')
        meshoy=int(input('Ingrese mes en el que estamos(ej:5):'))
        equipo=self.Buscar(id)
        lista=equipo.getContratos()
        if(len(lista)==0):
            print('El equipo no tiene contrato con ningun jugador!')
        else:
            for i in equipo.getContratos():
                fechaf=i.getFechaf()
                mesf=int(fechaf[fechaf.find('/')+1:fechaf.find('/2')])
                mesf=mesf-6
                if mesf <= meshoy:
                    print('A estos jugadores se les vence en 6 meses el contrato:')
                    print('----------')
                    print(i.getJugador())
                    print('----------')
    def ImportedeContratos(self):
        contador=0.0
        print('-------------Importe de Contratos-------------')
        id=input('Ingrese nombre del equipo:')
        equipo=self.Buscar(id)
        lista=equipo.getContratos()
        if(len(lista)==0):
            print('El equipo no tiene contrato con ningun jugador!')
        else:
            for i in equipo.getContratos():
                contador+=i.getPago()
            print('La cantidad que debe pagar el club es:{:.2f}'.format(contador))
