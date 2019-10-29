import os
os.system("cls")

# Definir productos y precios

productos = ["arrozcosteño", "cocacolapersonal", "inkakolapersonal", "chocolatesorrento", "snickers", "papaslays", "pringles", 
"detergenteariel", "galletascasino", "galletaschaplin", "chocolatevicio", "ajinosillao", "ketchupalacena", 
"cubosmaggie", "ajinomen"]
precios = [2.50,2.00,1.50,2.50,3.50,1.50,5.00,3.50,1.20,1.00,2.00,7.00,4.00,3.50,2.50]
stock = [20,15,15,16,12,25,25,10,14,5,10,15,10,20,50]
comprados = []
cantidad_comprados = []

# Cuando el cajero digita los productos:

i = 1
while True:
    entrada=input("Ingrese el producto " + str(i) + " : ")
    entrada = entrada.lower()
    entrada = entrada.replace(" ","")
    for p in range(0, len(productos)):
        if (entrada == ""):
            print("Tiene que ingresar un producto.")
            break
        elif entrada == productos[p]:
            i += 1
            comprados.append(entrada)
            break
    if comprados.count(entrada) == 0:
        print("El producto ha sido insertado incorrectamente.")
    else:
        elbooleano = input("¿Insertar más productos a la boleta?(Sí/No): ")
        elbooleano = elbooleano.lower()
        elbooleano = elbooleano.replace("í", "i")
        elbooleano = elbooleano.replace(" ","")
        if elbooleano == "no":
            break

while True:
    for i in range(0,len(comprados)):
        cantidad = int(input("Ingrese la cantidad del producto " + comprados[i] + " : "))
        if cantidad > 0:
            cantidad_comprados.append(cantidad)

    if len(cantidad_comprados) == len(comprados):
        break


print(comprados)
print(cantidad_comprados)