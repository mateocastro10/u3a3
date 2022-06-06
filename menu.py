from datetime import date
from manejadorcontrato import ManejaContrato
from manejadorequipos import ManejaEquipo
from manejadorjugador import ManejaJugador
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6,
                         '7':self.salir}
    def opcion(self,op,ManejadorJ,ManejadorC,ManejadorE):
        func=self.__switcher.get(op,lambda:'opcion incorrecta!')
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6'):
            func(ManejadorJ,ManejadorC,ManejadorE)
        else:
            func()
    def opcion1(self,ManejadorJ,ManejadorC,ManejadorE):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorJ.crearJugador()
    def opcion2(self,ManejadorJ,ManejadorC,ManejadorE):
        print('----------------Contrato----------------')
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorJ.mostrarJugadores()
            nombre=input('Ingrese nombre de jugador a contratar:')
            jugador=ManejadorJ.Buscar(nombre)
            if(jugador!=None):
                ManejadorE.mostrarEquipos()
                nombreE=input('Ingrese nombre de equipo que va a contratar:')
                equipo=ManejadorE.Buscar(nombreE)
                if(equipo!=None):
                    print('----------------Creacion de Contrato----------------')
                    año1=str(input('Ingrese Año de inicio del contrato:'))
                    mes1=str(input('Ingrese Mes de inicio del contrato:'))
                    dia1=str(input('Ingrese Dia de inicio del contrato:'))
                    fechai=dia1+'/'+mes1+'/'+año1
                    año=input('Ingrese Año de finalizacion del contrato:')
                    mes=input('Ingrese Mes de finalizacion del contrato:')
                    dia=input('Ingrese Dia de finalizacion del contrato:')
                    fechaf=dia+'/'+mes+'/'+año
                    pago=float(input('Ingrese Pago mensual del jugador:'))
                    contrato=ManejadorC.crearContrato(fechai,fechaf,pago,jugador,equipo)
                    equipo.agregarContrato(contrato)
                    print('.............Contrato Creado.............')
    def opcion3(self,ManejadorJ,ManejadorC,ManejadorE):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorC.MostrarContrato()
    def opcion4(self,ManejadorJ,ManejadorC,ManejadorE):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorE.ConsultarContratos()
    def opcion5(self,ManejadorJ,ManejadorC,ManejadorE):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorE.ImportedeContratos()
    def opcion6(self,ManejadorJ,ManejadorC,ManejadorE):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador and type(ManejadorE)==ManejaEquipo):
            ManejadorC.ArchivoContrato()
    def salir(self):
        return ('adios....')
