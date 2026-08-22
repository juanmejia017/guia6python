from .validaciones import validar_nombre, validar_edad

# Simulación de una base de datos en memoria usando una lista
_usuarios = []

def registrar_usuario(nombre: str, edad_str: str):
    try:
        nombre_valido = validar_nombre(nombre)
        edad_valida = validar_edad(edad_str)
        
        # Validar que no exista un usuario con el mismo nombre
        for u in _usuarios:
            if u['nombre'].lower() == nombre_valido.lower():
                raise ValueError(f"El usuario '{nombre_valido}' ya existe en el sistema.")
                
        nuevo_usuario = {"nombre": nombre_valido, "edad": edad_valida}
        _usuarios.append(nuevo_usuario)
        print(f"✅ Éxito: Usuario '{nombre_valido}' registrado correctamente.")
        
    except ValueError as e:
        print(f"❌ Error al registrar: {e}")

def listar_usuarios():
    if not _usuarios:
        print("⚠️ No hay usuarios registrados actualmente.")
        return
    
    print("\n--- Lista de Usuarios Registrados ---")
    for i, u in enumerate(_usuarios, 1):
        print(f"{i}. Nombre: {u['nombre']} | Edad: {u['edad']}")
    print("-------------------------------------\n")

def buscar_usuario(termino: str):
    termino = termino.strip().lower()
    if not termino:
        print("❌ Error: Debe ingresar un nombre para buscar.")
        return

    resultados = [u for u in _usuarios if termino in u['nombre'].lower()]
    
    if not resultados:
        print(f"⚠️ No se encontraron usuarios que coincidan con '{termino}'.")
        return
        
    print(f"\n--- Resultados de búsqueda para '{termino}' ---")
    for u in resultados:
        print(f"- Nombre: {u['nombre']} | Edad: {u['edad']}")
    print("-------------------------------------------\n")
