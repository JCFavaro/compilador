from typing import Dict


class Tabla():        
    
    class __Tabla:
        def _init_(self):
            self.ts = []
        
    def searchID(self, ID):
        for d in self.ts: #Aca busco en todos los contextos
            return ID in d
    
    def searchIDLocal(self, ID):    
        for d in self.ts[-1]: #Busco en solo 1 contexto
            return ID in d
        
    def addID(self, variable):
        self.ts[-1].append(variable.nombre, variable)
    
    def addContext(self):
        self.ts.append(dict())
    
    def deleteContext(self):
        self.ts[-1]
    
    
    
    