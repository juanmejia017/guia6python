import sys
from app.config import settings
from app.usuarios import gestor

def mostrar_menu():
    print(f"\n=== {settings.APP_NAME} v{settings.APP_VERSION} ===")
    print(f"Usuario Administrador: {settings.ADMIN_USER}")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir del sistema")
    print("=======================================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            print("\n-- Registro de Nuevo Usuario --")
            nombre = input("Ingrese el nombre del usuario: ")
            edad = input("Ingrese la edad del usuario: ")
            gestor.registrar_usuario(nombre, edad)
            
        elif opcion == '2':
            gestor.listar_usuarios()
            
        elif opcion == '3':
            nombre = input("\nIngrese el nombre a buscar: ")
            gestor.buscar_usuario(nombre)
            
        elif opcion == '4':
            print("Cerrando el sistema. ¡Hasta luego!")
            sys.exit(0)
            
        else:
            print("❌ Opción no válida. Por favor, seleccione un número del 1 al 4.")

if __name__ == "__main__":
    main()
