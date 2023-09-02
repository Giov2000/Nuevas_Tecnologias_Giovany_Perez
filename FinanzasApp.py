

saldo = 0
acumIngresos = 0
acumEgresos = 0

IsOn = int(input("Ingrese 1 para inicializar la aplicación\n"))
while IsOn == 1:
    opcion = input("Ingrese una opción\n1.Ingresar un ingreso\n2.Ingresar un egreso\n3.Continuar\n")

    if opcion == "1":
        ingresos = int(input("Registre un ingreso: "))
        saldo += ingresos
        acumIngresos += 1
        print(f"Cantidad de ingresos: {acumIngresos}")
        print(f"Saldo actual: ${saldo}")

    elif opcion == "2":
        egresos = int(input("Registre un egreso: "))
        if egresos>saldo:
            print(f"Saldo insuficiente para el egreso, su saldo restante es ${saldo}")
        else:
            saldo -= egresos
            acumEgresos += 1
            print(f"Cantidad de ingresos: {acumEgresos}")
            print(f"Saldo actual: ${saldo}")

    elif opcion == "3":
        print(f"Saldo final: ${saldo}")
        IsOn = 0

    else:
        print("Ingrese una opción válida")