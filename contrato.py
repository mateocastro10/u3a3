class Contrato:
    __fdeinicio=''
    __fdefinalizacion=''
    __pagomensual=0.0
    __jugador=None
    __equipo=None
    def __init__(self,fdeinicio,fdefinalizacion,pagomensual,jugador,equipo):
        self.__fdeinicio=fdeinicio
        self.__fdefinalizacion=fdefinalizacion
        self.__pagomensual=pagomensual
        self.__equipo=equipo
        self.__jugador=jugador
    def getJugador(self):
        return self.__jugador
    def getEquipo(self):
        return self.__equipo
    def getFechaf(self):
        return self.__fdefinalizacion
    def getFechai(self):
        return self.__fdeinicio
    def getPago(self):
        return self.__pagomensual
