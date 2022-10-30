# Generated from /home/fava/Documents/IUA/3/DHS/compilador/src/main/python/iua/compiladores.g4 by ANTLR 4.9.2
from ast import Delete
from hashlib import new
from multiprocessing.connection import deliver_challenge
from antlr4 import *
from tabla import Tabla
from funcion import Funcion
from variable import Variable
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
        pass
    
    # Enter a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        # print ("Term tiene " + str(ctx.getChildCount()) + " hijos")
        # print ("Term -> text |" + ctx.getText() + "|")        
        pass
        
    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        # print ("Factor IN -> |" + ctx.getText() + "|")
        self.tablaSimbolos.addContext()        

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        # print ("Factor OUT -> |" + ctx.getText() + "|")     
        self.tablaSimbolos.deleteContext()                                
    
     # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):           
        print("Comienza el bloque " + ctx.getText())
        self.tablaSimbolos.addContext()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print(self.tablaSimbolos.ts)             
        self.f.write(str(self.tablaSimbolos.ts))        
        self.f.write("\n")
        
        self.tablaSimbolos.deleteContext()
        
        if(len(self.tablaSimbolos.ts) == 0):
            self.f.close()
        
        # print("Fin del bloque")                        
        
     # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass                              

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):        
        variable = Variable()
        
        var = ctx.getText()
        datos = ""                

        if var.startswith("int"):
            variable.tipo = "int"
            datos = var[3:]
        if var.startswith("float"):
            variable.tipo = "float"
            datos = var[5:]
        if var.startswith("double"):
            variable.tipo = "double"
            datos = var[6:]
        if var.startswith("string"):
            variable.tipo = "string"
            datos = var[6:]            
        
        if "," in datos:
            
            variables = datos.split(",")
            
            for dato in variables:                
                
                newVariable = Variable()                
                newVariable = variable
                
                if '=' in dato:              
                    nombre = dato.split("=")                    
                    newVariable.nombre = nombre[0]
                    print("New variable: ", newVariable.nombre)
                    newVariable.inicializada = True
                    newVariable.usada = False
                    
                    self.tablaSimbolos.addID(newVariable)           
                else:
                    newVariable.nombre = dato
                    print("New variable sin = ", newVariable.nombre)                                        
                    newVariable.inicializada = False
                    newVariable.usada = False
                    
                    self.tablaSimbolos.addID(newVariable)                            
        elif "=" in datos:     
            datos = datos.split("=")
            variable.nombre = datos[0]
            variable.inicializada = True
            variable.usada = False 
            print("Variable ", variable.nombre)                             
            self.tablaSimbolos.addID(variable)        
        #En caso que sea por ej solo int a;
        else:
            variable.nombre = datos
            variable.inicializada = False
            variable.usada = False
            print(variable.nombre)
            self.tablaSimbolos.addID(variable)                              

    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):     
        pass
        
        # Enter a parse tree produced by compiladoresParser#decfuncion.
    def enterDecfuncion(self, ctx:compiladoresParser.DecfuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#decfuncion.
    def exitDecfuncion(self, ctx:compiladoresParser.DecfuncionContext):             
        funcion = Funcion()
        
        var = ctx.getText()
        
        datos = ""                

        if var.startswith("int"):
            funcion.tipo = "int"
            datos = var[3:]
        if var.startswith("float"):
            funcion.tipo = "float"
            datos = var[5:]
        if var.startswith("double"):
            funcion.tipo = "double"
            datos = var[6:]
        if var.startswith("string"):
            funcion.tipo = "string"
            datos = var[6:]            
        
        datos = datos.split("(")
        
        funcion.nombre = datos[0]
        
        datos = datos[1].split(')')[0]

        if "," in datos:
            parametros = datos.split(",")
            tipo = ""

            for parametro in parametros:
                if "int" in parametro:
                  tipo = "int"
                  nombre = parametro[3:]
                elif "string" in parametro:
                  tipo = "string"
                  nombre = parametro[6:]
                elif "float" in parametro:
                  tipo = "float"
                  nombre = parametro[5:]
                elif "double" in parametro:
                  tipo = "double"
                  nombre = parametro[6:]             
                else:
                  nombre = parametro
                funcion.addParametro(nombre,tipo)
        
        funcion.inicializada = True
        funcion.usada = False
                        
        self.tablaSimbolos.addID(funcion)                    

    # Enter a parse tree produced by compiladoresParser#deffuncion.
    def enterDeffuncion(self, ctx:compiladoresParser.DeffuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#deffuncion.
    def exitDeffuncion(self, ctx:compiladoresParser.DeffuncionContext):          
        funcion = Funcion()
        
        var = ctx.getText()
        datos = ""             

        if var.startswith("int"):
            funcion.tipo = "int"
            datos = var[3:]
        if var.startswith("float"):
            funcion.tipo = "float"
            datos = var[5:]
        if var.startswith("double"):
            funcion.tipo = "double"
            datos = var[6:]
        if var.startswith("string"):
            funcion.tipo = "string"
            datos = var[6:]            
        
        datos = datos.split("(")
        
        funcion.nombre = datos[0]        
        
        datos = datos[1].split(')')[0]
        
        nombre = ""
        tipo = ""        
        
        if "," in datos:            
            parametros = datos.split(",")            

            for parametro in parametros:                
                if "int" in parametro:                    
                    tipo = "int"
                    nombre = parametro[3:]                    
                elif "string" in parametro:
                    tipo = "string"
                    nombre = parametro[6:]
                elif "float" in parametro:
                    tipo = "float"
                    nombre = parametro[5:]
                elif "double" in parametro:
                    tipo = "double"
                    nombre = parametro[6:]             
                else:
                  nombre = parametro
                  
                funcion.addParametro(nombre,tipo)
                    
                funcion.inicializada = True
                funcion.usada = False
                
                self.tablaSimbolos.addID(funcion)
        elif len(datos) > 1: #tiene 1 solo parametro                        
            if "int" in datos:
                tipo = "int"
                nombre = datos[3:]
            elif "string" in datos:
                tipo = "string"
                nombre = datos[6:]
            elif "float" in datos:
                tipo = "float"
                nombre = datos[5:]
            elif "double" in datos:
                tipo = "double"
                nombre = datos[6:]             
            
            funcion.addParametro(nombre,tipo)
        
            funcion.inicializada = True
            funcion.usada = False
        
            self.tablaSimbolos.addID(funcion)    
            
        else: #Si no tiene parametros                   
            if "int" in datos:
                tipo = "int"
                nombre = datos[3:]
            elif "string" in datos:
                tipo = "string"
                nombre = datos[6:]
            elif "float" in datos:
                tipo = "float"
                nombre = datos[5:]
            elif "double" in datos:
                tipo = "double"
                nombre = datos[6:]             
            
            funcion.addParametro(nombre,tipo)
        
            funcion.inicializada = True
            funcion.usada = False
        
            self.tablaSimbolos.addID(funcion)                            

    # Enter a parse tree produced by compiladoresParser#llamadafuncion.
    def enterLlamadafuncion(self, ctx:compiladoresParser.LlamadafuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamadafuncion.
    def exitLlamadafuncion(self, ctx:compiladoresParser.LlamadafuncionContext):
        pass