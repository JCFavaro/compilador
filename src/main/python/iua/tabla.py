from typing import Dict


class Tabla(object):
    
    _instance = None
    #Singleton
    def __new__(self):
        if self._instance is None:
            self._instance = super(Tabla, self).__new__(self)
            self.ts = []
        return self._instance
        
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
    
    
    
    