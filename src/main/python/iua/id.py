#Usamos el decorator @property para poder reusar el nombre del metodo y hacer los get y setters

class ID:
    
    nombre =""
    tipo =""
    inicializada = False
    usada = False
        
    @property
    def nombre(self, val):
        self.nombre = val
        
    def nombre(self):
        return self.nombre
    
    @property
    def setTipo(self, val):
        self.tipo = val
        
    def tipo(self):
        return self.tipo
    
    @property
    def inicializada(self, val):
        self.inicializada = val
        
    def inicializada(self):
        return self.inicializada
    
    @property
    def usada(self, val):
        self.usada = val
    
    def usada(self):
        return self.usada
    
    def getDescripcion(self):
        return str(self.tipo) + " " + str(self.nombre) + " ~~ fue inicializada: " + str(self.inicializada) + " ~~ fue usada: " + str(self.usada)