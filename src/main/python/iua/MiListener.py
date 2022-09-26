# Generated from /home/fava/Documents/IUA/3/DHS/compilador/src/main/python/iua/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
        print ("Term -> text |" + ctx.getText() + "|")
    
    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor IN -> |" + ctx.getText() + "|")

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        print ("Factor OUT -> |" + ctx.getText() + "|")
    