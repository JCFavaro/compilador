from antlr4 import *
from compiladoresParser import compiladoresParser
from compiladoresVisitor import compiladoresVisitor

class MiVisitor(compiladoresVisitor):
        
    contexto = 0

    def visitProg(self, ctx:compiladoresParser.ProgContext):
        print("Comienza el programa")
        r = super().visitProg(ctx)                
        print("Finaliza el programa")
        return r

    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        self.contexto += 1
        print("\tEntramos al contexto " + str(self.contexto))
        print("\t\tContenido |" + ctx.getText() + "|")
        print("\t\tBloque tiene " + str(ctx.getChildCount()) + " hijos")
        print("\t\t\tHijo 0 -> " + ctx.getChild(0).getText())
        print("\t\t\tHijo 2 -> " + ctx.getChild(2).getText())
        r = super().visitInstrucciones(ctx.getChild(1))
        print("\tSalimos del contexto " + str(self.contexto))
        self.contexto -= 1
        return
    
    