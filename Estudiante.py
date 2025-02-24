from Persona import Persona
class Estudiante(Persona):
    def __init__(self,nombre,edad,direccion,curso):
        self.__curso=curso
        
    def get_curso(self):
        return self.__curso
    
    def set_curso(self,curso):
        self.__curso=curso
        
    def __str__(self):
        pass