import os
os.system("cls")

# Definir productos y precios

productos = ["arrozcosteño", "cocacolapersonal", "inkakolapersonal", "chocolatesorrento", "snickers", "papaslays", "pringles", 
"detergenteariel", "galletascasino", "galletaschaplin", "chocolatevicio", "ajinosillao", "ketchupalacena", 
"cubosmaggie", "ajinomen"]
precios = [2.50,2.00,1.50,2.50,3.50,1.50,5.00,3.50,1.20,1.00,2.00,7.00,4.00,3.50,2.50]
stock = [20,15,15,16,12,25,25,10,14,15,10,15,10,20,50]
comprados = []
cantidad_comprados = []

# Cuando el cajero digita los productos:

nombre_empresa = input("Ingrese el nombre de su mini-market: ")
print("Bienvenidos a " + nombre_empresa + "\n")
nombre_empresa = nombre_empresa.lower()
if nombre_empresa == "gaa":
    print ("aea mongol")

print("Productos del minimarket: ")
print(str(productos) + "\n")

i = 1
while True:
    #Se piden los productos que se están registrando y se modifica lo escrito para que sea 
    #válido con el arreglo "productos":
    entrada = input("Ingrese el producto " + str(i) + " : ")
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
            #Actualizacion del stock
            stock[productos.index(comprados[d])] = stock[productos.index(comprados[d])] - cantidad
            #Avisar al usuario del stock agotado
            if stock[productos.index(comprados[d])] == 0:
                print("El stock de "+ comprados[d]+" se ha acabado." )
            #Avisar el stock está apunto de acabarse    
            elif  stock[productos.index(comprados[d])] <=5:
                print("El stock de "+ comprados[d]+" está a punto de agotarse." )
              
            d += 1

                
        else:
            print("No hay suficiente cantidad del producto requerido.")
            
    else:
        print("Debe ingresar una cantidad válida.")

#Calcular total a pagar:
a = 0
total_pagar = 0
for i in comprados:
    total_pagar = total_pagar + (cantidad_comprados[a] * precios[productos.index(comprados[a])])
    a += 1

#Información del cliente , métodos de pago :
vuelto = 0
nombre = input("Ingrese el nombre del cliente: ")
while True:
#método de pago
    metodo = input("¿Pagará con tarjeta o efectivo? ")
    metodo = metodo.lower()
    metodo = metodo.replace(" ","")

    if metodo== "tarjeta":
        
        numero=[]
        while True:
            traj = input("¿Visa o Mastercard? ")
            traj = traj.lower()
            traj = traj.replace(" ","")
            numero = []
            if traj == "visa":
                while True:
                    numero = []
                    tarjeta_a_usar = int(input("Ingrese un numero de tarjeta de credito valido: "))
                    for i in str(tarjeta_a_usar):
                        numero.append(i)
                    if len(numero) == 16 and numero[0] == "4":
                        break
                    else:
                        print("Numero de tarjeta no valido para visa")
                break
            if traj == "mastercard":
                while True:
                    numero = []
                    tarjeta_a_usar = int(input("Ingrese un numero de tarjeta de credito valido: "))
                    for i in str(tarjeta_a_usar):
                        numero.append(i)
                    if len(numero) == 16 and numero[0] == "5":
                        break
                    else:
                        print("Numero de tarjeta no valido para mastercard")
                break
            else:
                print("Metodo de pago no valido, ingrese un tipo de tarjeta afiliada")                                                  
        break
    elif metodo=="efectivo":
        print(metodo)
        while True:
            dinero_a_ingresar = float(input("Ingrese cantidad de dinero depositado: "))
            if dinero_a_ingresar > 0:
                if dinero_a_ingresar >= total_pagar:
                    vuelto = dinero_a_ingresar - total_pagar                    
                    break
    
                else:
                    residuo = total_pagar - dinero_a_ingresar
                    print("Cantidad insuficiente, faltan s/. " + str(residuo))
            else:
                print("Cantidad de dinero no valida")
        break
    else:
        print("Ingrese un método válido.")

for q in range(0, len(comprados)):
    para_el_precio = productos.index(comprados[q])
    para_el_precio2 = precios[para_el_precio]
    cantidad_de_producto = cantidad_comprados[q]
    resultado = (para_el_precio2*cantidad_de_producto)
    resultado = round(resultado,2)
    

igv = total_pagar*(18/100)
igv = round(igv,2)
total_total = total_pagar + igv

#Su Real Boleta

nombre = nombre.capitalize()
#son 10 tabs para el centro
print( "\n" + "*********** Boleta de pago ***********")
print("Nombre del cliente: " + nombre)
if metodo == "tarjeta":
    metodo = metodo.capitalize()
    print("Método de pago: " + metodo)
    print("Número de tarjeta: " + str(tarjeta_a_usar))
    dinero_a_ingresar = total_total
elif metodo == "efectivo":
    print("Método de pago: " + metodo.capitalize())
print("Cliente pago con: S/. " + str(dinero_a_ingresar))
print("Tipo de moneda: Nuevo sol" + "\n")
print("Compras realizadas:")
for q in range(0, len(comprados)):
    print(comprados[q] + ": " + str(cantidad_comprados[q]) + " x S/." + str(para_el_precio2) + " = S/. " + str(resultado))
print("Precio neto: S/." + str(total_pagar))
print("IGV: S/." + str(igv))
print("Total a pagar: S/." + str(total_total))
vuelto -= igv
if metodo == "efectivo":
    print("Su vuelto va a ser de: S/." , vuelto, "\n")
print("Gracias por visitar " + nombre_empresa + "\n")