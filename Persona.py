class persona:
    def __init__(self,nombre,direccion,edad):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__edad=edad
      
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre= nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad = edad
        
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion):
        self.__direccion = direccion
        
    def __str__(self):
        print("la lista de estudiantes es: ", self.__nombre)
    
 
    
