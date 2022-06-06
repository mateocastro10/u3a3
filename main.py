from menu import Menu
from manejadorjugador import ManejaJugador
from manejadorcontrato import ManejaContrato
from manejadorequipos import ManejaEquipo
if __name__=='__main__':
    menu=Menu()
    manejadorJ=ManejaJugador()
    manejadorC=ManejaContrato()
    manejadorE=ManejaEquipo()
    manejadorE.LeerArchivo()
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.Crear un Jugador o Aleatorio')
        print('2.Crear Contrato')
        print('3.Consultar Jugador Contratado')
        print('4.Consultar Contratos')
        print('5.Obtener importe de contratos')
        print('6.Crear archivo con los contratos')
        print('7.Salir')
        op=input('->')
        print('------------------------------------------')
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6'):
            menu.opcion(op,manejadorJ,manejadorC,manejadorE)
        salir = op =='7'
