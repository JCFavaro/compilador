from mailbox import NoSuchMailboxError


class Variable(id):
    
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.nombre = nombre
        self.tipo = tipo
        