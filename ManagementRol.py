class Rol:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Rol:         {self.nombre}\nDescripción: {self.descripcion}"
    
    