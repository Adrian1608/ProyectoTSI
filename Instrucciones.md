# La Caja de ZuZu

###### La Caja de ZuZu es un software dirigido a mini-markets, que será usado con la función de generar boletas y registrar pagos a partir de información que guarada la misma app, y podrá avisar el estado actual del stock de cierto producto. Este software se desarrolló con el fin de facilitar el trabajo de los empleados de la tienda en cuestión, con apoyo de la tecnología que La Caja de ZuZu provee. Finalmente, este software se ha desarrollado para ser usado por los cajeros de los mini-markets, se necesita un nivel básico de conocimiento del uso de computadoras. 

###### Para usar La Caja de ZuZu, el empleado en cuestión debe tener abierto el software en Visual Studio Code, y cuando ejecute la aplicación, debe insertar los productos que el cliente está comprando. Al hacer esto, se le preguntará constantemente si desea añadir más productos a la boleta, a lo cual deberá responder "Sí" o "No" acorde al caso, y una vez termine de insertar los datos, se le consultará la cantidad comprada de cada producto insertado. Luego se le consultará el nombre del cliente al cajero, y se dará a elegir el pago entre efectivo o con tarjeta, y acorde a esto finalmente se calculará el pago total, usando los precios guardados en la misma aplicación.

###### El sistema con la información insertada se encargará de multiplicar el precio por la cantidad de cada producto comprado para calcular el precio total, así mismo disminuirá el stock acorde a los productos comprados y avisará cuánto de este hay en caso haya poco o nada. Finalmente, en la elección de método de pago, se definirá la sustracción de dinero de la tarjeta o el vuelto que se debe dar al cliente en caso sea efectivo, y se entregará la boleta validando la compra.

###### La Caja de ZuZu es un proyecto original, y cumple con sus funciones correctamente mientras los datos solicitados se inserten, y si este no fuera el caso, constantemente pedirá la información correcta al usuario.

###### La Caja de Zuzu actualmente en caso sea necesario, requiere una actualización constante de los precios de manera manual, además que si hubieran nuevos productos y nuevos precios, además de stock, se necesitaría también insertar esos datos. Y la información referente a estos productos se reinicia cada vez que se vuelve a usar la aplicación.

###### Para crear la Caja de ZuZu se ha usado el lenguaje Python, y la plataforma de desarrollo Python v3, y todo esto con la facilidad de usar el Entorno de Desarrollo Integrado Visual Studio Code.

###### La primera parte de este proyecto fue la implementación de los productos con sus precios y stocks mediante arreglos, y luego se implementaron los "inputs" para permitir la interacción entre el usuario y la computadora y llegar a la solución. Mediante estructuras de decisión y repetición se ha logrado también poder verificar correctamente qué productos se están alterando, e identificar sus precios y stock. Para generar la boleta de pago, se ha usado toda la información previa.

###### Si se insertan datos incorrectos, específicamente letras en vez de números o viceversa donde no es, el sistema fallará, por lo cual los empleados deben tener precaución con lo que insertan y no apresurarse arriesgándose a causar errores.

###### Para utilizar La Caja de ZuZu se deben seguir los siguientes pasos, desde el escritorio:

- Insertar en la barra de búsqueda "Visual Studio Code"
- Ejecutar Visual Studio Code
- Buscar en la barra a la izquierda un botón con 3 bloques unidos y 1 separado llamado "Extensions"
- Insertar en la barra de búsqueda "Python"
- Elegir la primera opción y darle al botón verde "Install"
- Insertar en la barra de búsqueda "Code Runner"
- Elegir la primera opción y darle al botón verde "Install"
- Buscar en la barra superior de la aplicación la opción "File"
- Abrir "File" y elegir el ítem de menu "Open File..."
- Buscar en la computadora el archivo Python de La Caja de ZuZu
- Abrir el archivo de la Caja de ZuZu con Visual Studio Code
- Buscar en la barra superior a la derecha el botón "Run Code" y presionarlo
- Utilizar la Caja de ZuZu

###### Para usar La Caja de ZuZu es necesario instalar el Entorno de Desarrollo Integrado Visual Studio Code, y además, se necesita obligatoriamente la extensión de Python del mismo entorno. También para darle facilidad a los empleados, se usa Code Runner, aunque este no es completamente necesario, pues con el click derecho y "Run Python File in Terminal..." se puede ejecutar de igual manera la aplicación.