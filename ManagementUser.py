from ManagementRol import Rol
class Usuario:
    def __init__(self, nombre, apellido, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}\nRol:    {self.rol.nombre}"
    