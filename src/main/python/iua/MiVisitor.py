from antlr4 import *
from compiladoresParser import compiladoresParser
from compiladoresVisitor import compiladoresVisitor

class MiVisitor(compiladoresVisitor):
        
    compiladores = 0
        
    def visitProg(self, ctx:compiladoresParser.ProgContext):
        print("Comienza el programa")
        r = super().visitProg(ctx)                
        print("Finaliza el programa")
        return r
    
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.contexto += 1
        print("\t Entramos al contexto " + str(self.contexto))
        r = super().visitInstrucciones(ctx.getChild())
        print("\t Salimos del contexto " + str(self.contexto))
        self.contexto -= 1
        return r

    
    
    