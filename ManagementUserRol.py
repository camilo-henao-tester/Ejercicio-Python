# Archivo: menu_usuarios.py
from ManagementRol import Rol  # Importamos la clase Rol desde rol.py
from ManagementUser import Usuario  # Importamos la clase Usuario desde usuario.py
import functools

class MenuUsuarios:
    def __init__(self):
        self.roles = []
        self.usuarios = []

    def agregar_rol(self, rol):
        self.roles.append(rol)
        print("\033[1;32m"+"Rol agregado exitosamente"+"\033[0;m")
    def agregar_rol_con_indice(self, rol, i):
        self.roles.insert(i, rol)
        print("\033[1;32m"+"Rol remplazado exitosamente"+"\033[0;m")

    def mostrar_roles(self):
        if not self.roles:
            print ("No hay roles creados, por favor elija otra opción")
        for rol in self.roles:
            print(rol)

    def crear_usuario(self, nombre, apellido, nombre_rol):
        rol_encontrado = None
        for rol in self.roles:
            if rol.nombre == nombre_rol:
                rol_encontrado = rol
                break
        if rol_encontrado:
            usuario = Usuario(nombre, apellido, rol_encontrado)
            self.usuarios.append(usuario)
            print("\033[1;32m"+f"Usuario {nombre} {apellido} creado con éxito."+"\033[0;m")
        else:
            print(f"No se encontró el rol {nombre_rol}.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print ("No hay usuarios creados, por favor elija otra opción")
        for usuario in self.usuarios:
            print(usuario)

    def reemplazar_rol(self, nombre_rol):
        for i in range(len(self.roles)):
            if self.roles[i].nombre == nombre_rol:
                self.roles.remove(self.roles[i])
                print("\033[1;32m"+f"Rol {nombre_rol} eliminado correctamente."+"\033[0;m")
                return i
        else:
            print(f"No se encontró el rol {nombre_rol}.")
            return 0

    def actualizar_rol(self, nombre_rol, nueva_descripcion):
        for rol in self.roles:
            if rol.nombre == nombre_rol:
                rol.descripcion = nueva_descripcion
                print("\033[1;32m"+f"Rol {nombre_rol} actualizado correctamente."+"\033[0;m")
                break
        else:
            print(f"No se encontró el rol {nombre_rol}.")
                   
    #decoradores   
    def actualizar_lista(funcion):
        def wrapper(self,  *args, **kwargs):
            if args[1] == 1:
                self.roles = funcion( *args, **kwargs)
            else:
                self.usuarios = funcion( *args, **kwargs)
            
            return "\033[1;32m"+"Lista actualizada"+"\033[0;m"
        return wrapper        
    def buscar(funcion):
        def wrapper(*args, **kwargs):
            lista = funcion(*args, **kwargs)
            for ele in lista:
                if ele.nombre == args[2]:
                    lista.remove(ele)
                    print("\033[1;32m"+f"{ele.nombre} eliminado correctamente."+"\033[0;m")
                    break
            else:
                print(f"{args[2]} no fue encontrado")
            return lista
        return wrapper
    
    @actualizar_lista
    @buscar
    def eliminar(self,tipo, nombre):        
        if tipo == 1:
            lst = self.roles
        else:
            lst= self.usuarios
        return lst
    
    
    
    
   
        
        


   
