from distutils.log import error
from typing import Dict


class Tabla(object):
    
    _instance = None
    
    #Singleton
    def __new__(self):
        if self._instance is None:
            self._instance = super(Tabla, self).__new__(self)            
            self.ts = [dict()]
        return self._instance
        
    def searchID(self, ID):
        for d in self.ts: #Aca busco en todos los contextos
            return ID in d
    
    def searchIDLocal(self, ID):    
        for d in self.ts[-1]: #Busco en solo 1 contexto
            return ID in d
        
    def searchNameLocal(self, nombre):
        for var in self.ts[-1]:
            if nombre in var:
                return var.tipo
        
    def addID(self, variable):   #puse variable pero tmb vienen funciones
        self.ts[-1].update({"Nombre": variable.nombre, "Tipo": variable.tipo, "Inicializada": variable.inicializada, "Usada": variable.usada})
        
    def addContext(self):
        self.ts.append(dict())
    
    def deleteContext(self):                
        self.ts.pop()
        