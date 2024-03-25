from ManagementRol import Rol
from ManagementUser import Usuario
from ManagementUserRol import MenuUsuarios

class Menu:
    
    def Printmenu(self, menu_usuarios):
        self.menu_usuarios = MenuUsuarios()
        print("""
╔════════════════════════════════════════╗
║    Elige una opción:                   ║
║       1. Crear un rol                  ║
║       2. Eliminar un rol               ║
║       3. Crear un usuario              ║
║       4. Remplazar rol                 ║
║       5. Modificar descripción del rol ║
║       6. Eliminar usuario              ║
║       7. Mostrar roles                 ║
║       8. Mostrar usuarios              ║
║       0. Salir                         ║
╚════════════════════════════════════════╝ """)
        
        opc = input("\033[1;33m"+"-> ""\033[0;m")

        if opc == "1":
            # Capturar datos para crear roles
            print("Ingrese los datos para crear roles:")
            nombre_rol = input("Nombre del rol: ")
            descripcion_rol = input("Descripción del rol: ")
            rol_nuevo = Rol(nombre_rol, descripcion_rol)
            menu_usuarios.agregar_rol(rol_nuevo)
        elif opc == "2":
            # Capturar datos para eliminar un rol
            nombre_rol_eliminar = input("\nIngrese el nombre del rol que desea eliminar: ")    
            menu_usuarios.eliminar(menu_usuarios,1,nombre_rol_eliminar)
        elif opc == "3":
            # Capturar datos para crear usuarios
            print("\nIngrese los datos para crear un usuario:")
            nombre_usuario = input("Nombre del usuario: ")
            apellido_usuario = input("Apellido del usuario: ")
            nombre_rol_usuario = input("Nombre del rol del usuario: ")
            menu_usuarios.crear_usuario(nombre_usuario, apellido_usuario, nombre_rol_usuario)
        elif opc == "4":
            # Capturar datos para eliminar un rol
            nombre_rol_eliminar = input("\nIngrese el nombre del rol que desea reemplazar: ")    
            i=menu_usuarios.reemplazar_rol(nombre_rol_eliminar)
            if i:
                print("Ingrese los datos para reemplazar el rol eliminado:")
                nombre_rol = input("Nombre del nuevo rol: ")
                descripcion_rol = input("Descripción del nuevo rol: ")
                rol_nuevo = Rol(nombre_rol, descripcion_rol)
                menu_usuarios.agregar_rol_con_indice(rol_nuevo,i)     
        elif opc == "5":
            # Capturar datos para actualizar un rol
            nombre_rol_actualizar = input("\nIngrese el nombre del rol que desea actualizar: ")
            nueva_descripcion_rol = input("Ingrese la nueva descripción para el rol: ")
            menu_usuarios.actualizar_rol(nombre_rol_actualizar, nueva_descripcion_rol)
            # Mostrar roles actualizados
            print("\nRoles actualizados:")
            menu_usuarios.mostrar_roles()
        elif opc == "6":
            # Capturar datos para eliminar un rol
            nombre_usuario_eliminar = input("\nIngrese el nombre del usuario que desea eliminar: ")         
            menu_usuarios.eliminar(menu_usuarios,0,nombre_usuario_eliminar)
        elif opc == "7":
            # Mostrar roles disponibles
            print("\nRoles disponibles:")
            menu_usuarios.mostrar_roles()
        elif opc == "8":
            # Mostrar usuarios creados
            print("\nUsuarios creados:")
            menu_usuarios.mostrar_usuarios()
        elif opc == "0":         
            return 0
        else:
            print("Elige una opción valida")     
        return 1