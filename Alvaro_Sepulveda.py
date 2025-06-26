from os import system 

usuarios = {"nombre" : None}

def limpiar_pantalla():
    try:
        system("cls")
        pass
    except:
        system("clear")

def main():
    while True:
        print("MENU PRINCIPAL")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")

        opcion = input("Ingrese opcion: ")
        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Opcion no valida. Intente de nuevo\n")

def opcion_1():
    usuarios['nombre'] = input("Ingrese nombre de usuario: ")
    while True:
        usuarios['sexo'] = input("Ingrese sexo: ")
        if usuarios['sexo'] == "F" or usuarios['sexo'] == "M":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")
    while True:
        usuarios['contraseña'] = input("Ingrese contraseña: ")
        hay_numero = any(c.isdigit() for c in usuarios['contraseña'])
        hay_mayuscula = any(c.islower() for c in usuarios['contraseña'])
        hay_minuscula = any(c.islower() for c in usuarios['contraseña'])
        hay_espacio = any(c == " " for c in usuarios['contraseña'])
        if len(usuarios['contraseña']) == 8 and hay_numero and hay_minuscula or len(usuarios['contraseña']) == 8 and hay_numero and hay_mayuscula:
            break
        elif len(usuarios['contraseña']) == 8 and hay_numero and hay_minuscula and hay_espacio or len(usuarios['contraseña']) == 8 and hay_numero and hay_mayuscula and hay_espacio:
            print("Contraseña no valida. Intente otra.")
        else:
            print("Contraseña no valida. Intente otra.")
    print("Usuario ingresado con exito!!\n")
    
def opcion_2():
    buscar_usuario = input("Ingrese usuario a buscar: ")
    if usuarios['nombre'] == buscar_usuario:
        print(f"El sexo del usuario es: {usuarios['sexo']} y la contraseña es: {usuarios['contraseña']}\n")
    else:
        print("El usuario no se encuentra.\n")

def opcion_3():
    eliminar_usuario = input("Ingrese usuario a eliminar: ")
    if usuarios['nombre'] == eliminar_usuario:
        del usuarios['nombre']
        print("Usuario eliminado con exito!\n")
    else:
        print("No se puedo eliminar usuario!\n")

limpiar_pantalla()
main()

