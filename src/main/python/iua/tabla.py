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
        
    def searchID(self, ID):#Aca busco en todos los contextos            
        return ID in self.ts   
                        
    def searchIDLocal(self, ID): #Busco en solo 1 contexto            
        for ctx in reversed(self.ts): #reversed para empezar desde -1
            keys = ctx.keys() 
            for key in keys:                
                if str(ID) == str(key):  
                    return ctx[key]                
                                                
    def addID(self, ID):                       
        self.ts[-1][ID.nombre] = ID        
        
    def addContext(self):
        self.ts.append(dict())
    
    def deleteContext(self):                
        self.ts.pop()
    
    def ctxString(self):                                  
        for ctx in self.ts:  
            values = ""               
            keys = ctx.keys()
            values += "------ Inicio Contexto -------\n"
            for key in keys:                      
                values += ctx[key].getDescripcion() + "\n"
            values += "------ Fin Contexto -------\n\n"            
        return values