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

nombre_empresa = input("Ingrese el nombre de su mini-market: ")
print("Bienvenidos a " + nombre_empresa + "\n")
if nombre_empresa == "gaa":
    print ("aea mongol")
i = 1
while True:
    #Se piden los productos que se están registrando y se modifica lo escrito para que sea 
    #válido con el arreglo "productos":
    entrada=input("Ingrese el producto " + str(i) + " : ")
    entrada = entrada.lower()
    entrada = entrada.replace(" ","")
    #Se lee el arreglo para verificar que el producto esté disponible:
    for p in range(0, len(productos)):
        if entrada == productos[p]:
            comprados.append(entrada)
            break
        elif entrada == (""):
            print("Debe ingresar un producto.")
            break
    #Esto verifica que el producto no se ingrese más veces:
    if comprados.count(entrada) > 1:
        print("El producto ya ha sido insertado.")
        comprados.remove(entrada)
    elif entrada != productos[p]:
        print("El producto no es válido.")
    else:
        #Modificar la entrada de Si o No para que sea válida para el sistema:
        elbooleano = input("¿Insertar más productos a la boleta?(Sí/No): ")
        elbooleano = elbooleano.lower()
        elbooleano = elbooleano.replace("í", "i")
        elbooleano = elbooleano.replace(" ","")
        i += 1
        if elbooleano == "no":
            break

#Pedir la cantidad de productos ingresados:
d = 0
while (len(comprados) != len(cantidad_comprados)):
    cantidad = int(input("Ingrese la cantidad del producto " + comprados[d] + " " + ":" + " "))
    if cantidad > 0:
        if cantidad <= stock[productos.index(comprados[d])]:
            cantidad_comprados.append(cantidad)
            stock[productos.index(comprados[d])] = stock[productos.index(comprados[d])] - cantidad
            d += 1
        else:
            print("No hay suficiente cantidad del producto requerido.")
            
    else:
        print("Debe ingresar una cantidad válida.")


print(comprados)
print(cantidad_comprados)
print(stock)
