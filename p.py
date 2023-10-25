class p1:
    def __init__(self, nombre, ape):
        self.nombre = nombre
        self.ape = ape

    def mi_nombre_es(self):
        return f"Mi nombre es {self.nombre} {self.ape} desde p1"
    

class p2:
    def __init__(self, nombre, ape):
        self.nombre = nombre
        self.ape = ape

    def mi_nombre_es(self):
        return f"Mi nombre es {self.nombre} {self.ape} desde p2"
    

class hereda(p2,p1):
    def __init__(self, nombre, ape):
        p1.__init__(self, nombre,ape)
        p2.__init__(self, nombre,ape)

    
dime = hereda("Yelitza","Suniaga")
print(p2.mi_nombre_es(dime))
