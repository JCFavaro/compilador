from id import ID

class Funcion(ID):
    
    parametros = []  
    
    def addParametro(self, nombre, tipo):
        self.parametros.append(dict())
        self.parametros[-1].update({"Tipo: ": tipo, "Nombre: ": nombre})