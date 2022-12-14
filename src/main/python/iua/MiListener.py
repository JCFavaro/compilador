# Generated from /home/fava/Documents/IUA/3/DHS/compilador/src/main/python/iua/compiladores.g4 by ANTLR 4.9.2
from ast import Delete
from hashlib import new
from multiprocessing.connection import deliver_challenge
from tokenize import String
from antlr4 import *
from tabla import Tabla
from funcion import Funcion
from variable import Variable
import re 
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MiListener(ParseTreeListener):

    context = None
    tablaSimbolos = Tabla()
    f = open("tablaDeSimbolos.txt", "w")    

     # Enter a parse tree produced by compiladoresParser#prog.
    def enterProg(self, ctx:compiladoresParser.ProgContext):                
        pass

    # Exit a parse tree produced by compiladoresParser#prog.
    def exitProg(self, ctx:compiladoresParser.ProgContext):                         
        print("Exit prog " + ctx.getText()) 
        self.f.write(self.tablaSimbolos.ctxString())        
        self.tablaSimbolos.deleteContext()        
        self.f.close()

    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):        
        pass

    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):        
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):        
        pass

     # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):                                      
        pass                   

     # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):                   
        self.tablaSimbolos.addContext()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):       
        print("termina el bloque " + ctx.getText())
        self.f.write(self.tablaSimbolos.ctxString())
        for variables in self.tablaSimbolos.ts:
            for var in variables:
                nombre = self.tablaSimbolos.searchIDLocal(var)
                if nombre.usada == False and nombre.inicializada == True:
                    print("variable", nombre.nombre, "no usada")
                elif nombre.inicializada == False:
                    print("variable", nombre.nombre, "no inicializada")
        self.tablaSimbolos.deleteContext()        

     # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass                              

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #Para variables inicializadas
        if ctx.getChild(1).getChild(0) != None:
            variable = Variable()
            variable.tipo = ctx.getChild(0).getChild(0)
            variable.nombre = ctx.getChild(1).getChild(0)            
            variable.inicializada = True
            variable.usada = False            
            if self.tablaSimbolos.searchIDLocal(variable.nombre) == None:
                self.tablaSimbolos.addID(variable)
            else:
                raise Exception("Variable declarada varias veces")
        #Para variables declaradas
        elif ctx.getChild(1).getChild(0) == None and ctx.getChildCount() < 3:  
            for data in range(0, ctx.getChildCount()):            
                if ctx.getChild(data).getChildCount() == 0:
                    variable = Variable()                     
                    variable.nombre = str(ctx.getChild(data))                                
                    variable.tipo = str(ctx.getChild(0).getChild(0))
                    variable.inicializada = False
                    variable.usada = False                                        
                    if self.tablaSimbolos.searchIDLocal(variable.nombre) == None:
                        self.tablaSimbolos.addID(variable)
                    else:
                        raise Exception("Variable declarada varias veces")
        else: #Significa que hay mas de una variable declarada int a,b,c...;
            for data in range(1, ctx.getChildCount(), 2):
                variable = Variable()       
                variable.tipo = str(ctx.getChild(0).getChild(0))
                variable.inicializada = False
                variable.usada = False                                    
                if ctx.getChild(data).getChildCount() == 0:
                    variable.nombre = str(ctx.getChild(data))                    
                    if self.tablaSimbolos.searchIDLocal(variable.nombre) == None:
                        self.tablaSimbolos.addID(variable)
                    else:
                        raise Exception("Variable declarada varias veces")

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):                     
        variableAsignada = Variable()        
        
        tiposVar = {"int", "float", "string", "double", "char"}
        
        if ctx.parentCtx.getChild(0).getChild(0) != None and str(ctx.parentCtx.getChild(0).getChild(0)) not in tiposVar:
            variableAsignada = self.tablaSimbolos.searchIDLocal(ctx.parentCtx.getChild(0).getChild(0))                    
            if variableAsignada != None:
                variableAsignada.inicializada = True
            else:
                print("Asignacion de variable no declarada", str(ctx.parentCtx.getChild(0).getChild(0)))
            
        if ctx.getChild(2).getChild(0) != None: #Asignacion con operaciones                         
            operandos = ctx.getChild(2).getText()            
            aux1 = re.split("[+*/-]", operandos)
            for op1 in aux1:
                try:
                    float(op1)
                except:
                    variableUsada = Variable()
                    variableUsada = self.tablaSimbolos.searchIDLocal(op1)
                    if variableUsada != None:
                        variableUsada.usada = True                    
        else: #Asignacion Sin operaciones ej: a = 3
            try:
                float(ctx.getChild(2))
            except:
                variableUsada = Variable() 
                variableUsada = self.tablaSimbolos.searchIDLocal(ctx.getChild(2))
                if variableUsada != None:
                    variableUsada.usada = True                

        # Enter a parse tree produced by compiladoresParser#decfuncion.
    def enterDecfuncion(self, ctx:compiladoresParser.DecfuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decfuncion.
    def exitDecfuncion(self, ctx:compiladoresParser.DecfuncionContext):                                 
        funcion = Funcion()                        
        tipoParametro = ""                                                  

        for data in range(3, ctx.getChildCount() - 2):  
                if ctx.getChild(data).getChildCount() != 0:                                                   
                    dato = ctx.getChild(data).getChild(0)
                    if(str(dato) != ","):
                        tipoParametro = str(dato)
                else:                    
                    dato = ctx.getChild(data)
                    if(str(dato) != ","):
                        funcion.addParametro(str(dato), tipoParametro)                        

        funcion.tipo = str(ctx.getChild(0).getChild(0))
        funcion.nombre = str(ctx.getChild(1))                       

        funcion.inicializada = False
        funcion.usada = False

        if self.tablaSimbolos.searchIDLocal(funcion.nombre) == None:
            self.tablaSimbolos.addID(funcion)
        else:
            raise Exception("Funcion declarada varias veces")

    # Enter a parse tree produced by compiladoresParser#deffuncion.
    def enterDeffuncion(self, ctx:compiladoresParser.DeffuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#deffuncion.
    def exitDeffuncion(self, ctx:compiladoresParser.DeffuncionContext):          
        funcion = Funcion()                        
        tipoParametro = ""                    

        funcion.tipo = str(ctx.getChild(0).getChild(0))
        funcion.nombre = str(ctx.getChild(1))       

        if ctx.getChildCount() > 5:    
            for data in range(3, ctx.getChildCount() - 2):  
                    if ctx.getChild(data).getChildCount() != 0:                                                   
                        dato = ctx.getChild(data).getChild(0)
                        if(str(dato) != ","):
                            tipoParametro = str(dato)
                    else:                    
                        dato = ctx.getChild(data)
                        if(str(dato) != ","):
                            funcion.addParametro(str(dato), tipoParametro)                        

        funcion.inicializada = True
        funcion.usada = False 

        if self.tablaSimbolos.searchIDLocal(funcion.nombre) == None:
            self.tablaSimbolos.addID(funcion)
        else:
            raise Exception("Funcion declarada varias veces")         

    # Enter a parse tree produced by compiladoresParser#llamadafuncion.
    def enterLlamadafuncion(self, ctx:compiladoresParser.LlamadafuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadafuncion.
    def exitLlamadafuncion(self, ctx:compiladoresParser.LlamadafuncionContext):
        funcion = Funcion()         

        nombre = str(ctx.getChild(0))

        funcion = self.tablaSimbolos.searchIDLocal(nombre)

        if funcion != None:
            if funcion.inicializada == False:
                print("Funcion", nombre, "declarada pero no definida")
            else:
                funcion.usada = True
        else:
            print("Funcion", nombre, "no declarada ni definida")
        