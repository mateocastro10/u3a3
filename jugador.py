class Jugador:
    __nombre=''
    __dni=''
    __ciudad=''
    __pais=''
    __fdenacimiento=''
    def __init__(self,nombre,dni,ciudad,pais,fdenacimiento):
        self.__nombre=nombre
        self.__dni=dni
        self.__ciudad=ciudad
        self.__pais=pais
        self.__fdenacimiento=fdenacimiento
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def __str__(self):
        return ('nombre:{}\ndni:{}\nciudad:{}\npais:{}\nfecha de nacimiento:{}'.format(self.__nombre,self.__dni,self.__ciudad,self.__pais,self.__fdenacimiento))
