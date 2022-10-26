from distutils.log import error
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
        # if variable.nombre in self.ts[-1]: print("Variable declarada mas de una vez")        
        self.ts[-1][variable.nombre, variable] 
    
    def addContext(self):
        self.ts.append(dict())
    
    def deleteContext(self):                
        del self.ts[-1]
        