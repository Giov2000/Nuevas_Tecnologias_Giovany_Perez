# 1. Recibir por consola el valor de una compra
# 2. Ingresar el numero de cuotas
# 3. Calcular el valor de la cuota
# 4. Usando ciclo while imprimir el plan de pago y
# mostrar el cupo liberado con cada pago

valorCompra = int(input("Ingrese el valor de la compra: "))
nroCuotas = int(input("Ingrese el numero de cuotas: "))

valorCuota = valorCompra/nroCuotas

while valorCompra!=0:
    print("\nValor del pago: ",valorCuota)
    valorCompra -= valorCuota
    print("Saldo Restante: ",valorCompra)
print("Ha pagado el total de la compra")
