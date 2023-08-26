from random import shuffle

list = ["a","1","b","2","c","3","d","4","e","5","f","6","g","7","h","8","i","9","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
shuffle(list)
characters = list[:6]
caplist = ""
for character in characters:
    caplist += character

email = "test@mail.com"
password = "123"

database = {}

def main():
    opcion = int(input("Ingrese una de las siguientes opciones: \n 1.Registrarse\n 2.Iniciar Sesion\n 3.Salir \n"))
    if opcion == 1:
        registrar()
    elif opcion == 2:
        inicioSesion()
    elif opcion == 3:
        print("Hasta pronto :)")
    else:
        print("Ingrese una opcion valida")
        main()

def registrar():
    inemail = input("Registre su correo: ")
    inpassword = input("Registre su contraseña: ")
    database[inemail] = inpassword
    main()

def inicioSesion():
    inemail = input("Ingrese su correo: ")
    inpassword = input("Ingrese su contraseña: ")
    if (inemail in database) and (database[inemail] == inpassword):
        rescap = input("Escribe el siguiente codigo: \n"+caplist+"\n")
        if(rescap in caplist):
            print("Hola usuario, has ingresado correctamente")
            tarjeta()
        else:
            print("El codigo ingresado es incorrecto")
    else:
        print("Error, correo o contraseña inválidos")
        inicioSesion()


def tarjeta():
    valorCompra = int(input("Ingrese el valor de la compra: "))
    nroCuotas = int(input("Ingrese el numero de cuotas: "))

    valorCuota = valorCompra/nroCuotas

    while valorCompra>0:
        print("\nValor del pago: ",valorCuota)
        valorCompra -= valorCuota
        print("Saldo Restante: ",valorCompra)
    print("Ha pagado el total de la compra")

main()

# print("1. Registro\n 2. Login \n 3. Salir")
# opc = 0
# if opc == 1:
#     print("Registro")
# elif opc == 2:
#     print("Login")
# elif opc == 3:
#     print("salir")
# else:
#     print("Seleccione una opcion Valida")
# Generar un programa que permita hacer el registro e iniciar sesion dentro de while,
# debe imprimir el menu usando la implementacion de if, elif , else (Selector multiple).
# Cuando inicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterio.
