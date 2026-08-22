def validar_nombre(nombre: str) -> str:
    nombre = nombre.strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
    return nombre

def validar_edad(edad_str: str) -> int:
    try:
        edad = int(edad_str)
    except ValueError:
        raise ValueError("La edad debe ser un número entero válido.")
    
    if edad < 0:
        raise ValueError("La edad no puede ser un número negativo.")
    if edad < 18:
        raise ValueError("El usuario debe ser mayor de edad (18+).")
    
    return edad
