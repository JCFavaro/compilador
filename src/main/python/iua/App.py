import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MiListener import MiListener
from MiVisitor import MiVisitor
from tabla import Tabla

tablaSimbolos = Tabla()

def main(argv):
    # archivo = "input/entrada.txt"
    # archivo = "input/operaciones.txt"
    archivo = "input/test.c"

    if len(argv) > 1 :
        archivo = argv[1]

    input = FileStream(archivo)

    lexer = compiladoresLexer(input)

    stream = CommonTokenStream(lexer)

    parser = compiladoresParser(stream)

    miListener = MiListener()

    parser.addParseListener(miListener)

    tree = parser.prog()
    
    miVisitor = MiVisitor()
    miVisitor.visitProg(tree)

    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)