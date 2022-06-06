import numpy as np
import csv
from contrato import Contrato
class ManejaContrato:
    __dimension=1
    __cantidad=0
    __incremento=1
    def __init__(self):
        self.__contratos=np.empty(self.__dimension,dtype=Contrato)
    def agregar(self,contrato):
        if(self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__contratos.resize(self.__dimension)
            self.__contratos[self.__cantidad]=contrato
            self.__cantidad+=1
        else:
            self.__contratos[self.__cantidad]=contrato
            self.__cantidad+=1
    def crearContrato(self,fechai,fechaf,pago,jugador,equipo):
        contrato1=Contrato(fechai,fechaf,pago,jugador,equipo)
        self.agregar(contrato1)
        return contrato1
    def MostrarContrato(self):
        i=0
        print('-------------Buscar Contratos-------------')
        dni=input('Ingrese DNI del jugador:')
        while((i<len(self.__contratos)) and (dni!=self.__contratos[i].getJugador().getDni())):
            i+=1
        if(i<len(self.__contratos)):
            print('Equipo:{} \n Fecha de Finalizacion:{}'.format(self.__contratos[i].getEquipo().getNombre(),self.__contratos[i].getFechaf()))
        else: print('Jugador no contratado!')
    def ArchivoContrato(self):
        with open('contratos.csv','w') as csvfile:
            cabecera=['DNI del jugador','Equipo','fecha de inicio','fecha de fin','pago mensual']
            writer=csv.writer(csvfile)
            writer.writerow(cabecera)
            for i in self.__contratos:
                writer.writerow([i.getJugador().getDni(),
                                i.getEquipo().getNombre(),
                                i.getFechai(),
                                i.getFechaf(),
                                i.getPago()])
        print('Archivo creado con exito!')
