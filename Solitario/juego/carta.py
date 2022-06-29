class Carta:
    def __init__(self, tipo, color, numero, representacion, visible):
        self._tipo = tipo
        self._color = color
        self._numero = numero
        self._representacion = representacion
        self._visible = visible
    
    def getTipo(self):
        return self._tipo
    
    def setTipo(self, tipo):
        self._tipo = tipo

    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color = color

    def getNumero(self):
        return self._numero
    
    def setNumero(self, numero):
        self._numero = numero

    def getRepresentacion(self):
        return self._representacion
    
    def setRepresentacion(self, representacion):
        self._representacion = representacion

    def isVisible(self):
        return self._visible
    
    def setVisible(self, visible):
        self._visible = visible