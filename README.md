# ParcialHerramientasComputacionales

### ¿Qué problema es?
El **problema** que se plantea y se busca resolver es el de realizar un programa para un sistema de descuentos en la cafetería de la Universidad Javeriana como ayuda para la situación económica de estudiantes y profesores debido a la pandemia. Este programa debe **solicitar los datos del cliente**, específicamente su cédula y rol dentro de la Universidad. Dependiendo de este último, el descuento será diferente: si el cliente es profesor, tendrá un 20% de descuento; si es estudiante, tendrá 50% de descuento. 

Además de esto, el programa debe requerir (en su versión inicial) el código del producto a adquirir, el precio de este y la cantidad que el cliente desea comprar. Después de ingresar esta información, el programa debe realizar los cálculos correspondientes de manera que pueda imprimir el total de la compra después de que se le ha aplicado el descuento, así como otros datos, de la siguiente forma:

> ”El **_rol_** con cédula **_número_**, debe pagar **_valor_** por el producto **_código_**”

### ¿Qué modelo computacional lo resuelve?
Este programa usa estructuras básicas de Python para resolver la situación planteada anteriormente. Mediante requerimientos de inputs por parte del usuario, condicionales, ciclos y cálculos simples se otorga respuesta a las necesidades expuestas. Un ejemplo de esto se puede observar abajo (todas las partes de código en este ReadMe se encuentran unificadas en el archivo **_parcialHerramientasVer4Final.py_** que está en este repositorio):

```python
checkFunc = input("¿Seguir registrando usuarios? (Si o No): ")

if checkFunc == "Si" or checkFunc == "Sí" or checkFunc == "SI" or checkFunc == "si" or checkFunc == "sí":
  funcionamiento = True
  ingresarProductos = True
  ans = ""
  ansParcial = ""
  totalSinDesc = 0
  print("--------------")
  
elif checkFunc == "No" or checkFunc == "NO" or checkFunc == "no":
  funcionamiento = False
 ```
 
En lo anterior se puede observar uno de los inputs que el usuario del programa debe ingresar durante su funcionamiento. De acuerdo con este input, con ayuda de los condicionales, se determina si el programa continúa registrando clientes (es decir, sigue iterando el ciclo dentro del cual se encuentra este condicional) o si termina el programa.

### ¿Qué recibe el algoritmo como entrada?
El programa recibe múltiples inputs por parte del usuario, algunos convirtiéndose a números enteros (ints) de manera que se posible operar con ellos, y otros dejándose como cadenas de texto (str): 

* **integers** - precio y unidades del producto a registrar
* **strings** - cédula y rol del cliente, así como el código del producto. 
<br>
Asimismo, después de imprimir la respuesta esperada, el algoritmo recibe dos inputs más para corroborar si el cliente desea que un ciclo particular del programa siga corriendo. Uno de estos es para verificar si el usuario desea registrar más productos y el otro es para saber si hay más clientes por pasar a la caja. Estos son inputs de cadena (str) que aceptan diferentes versiones de "Si" o "No".

### ¿Cuál es la salida esperada? 
En la versión final hay dos salidas esperadas. Debido a que el cliente puede ingresar varias cantidades de productos diferentes, entonces se va creando algo similar a una cuenta en la que se muestra la cédula y el rol del cliente, al igual que el código del producto y el precio con descuento de dicho producto (de acuerdo con las cantidades que la persona vaya a llevar).

```python
ansParcial = ansParcial + cedula + " debe pagar $" + str(totalParcial) + " por el producto " + codProducto + "."
```

Cabe aclarar que la primera parte de ansParcial varía de acuerdo con el rol ingresado por el usuario (profesora, profesor o estudiante).

Cuando se le pregunta al usuario si va a ingresar más productos, si este da una respuesta negativa, se imprime otro mensaje diferente con el total de la cuenta, así:

```python
ans = ans + cedula + " debe pagar $" + str(total) + " en total."
```

Si le gustaría leer información acerca de los posibles errores del programa así como un poco más de documentación respecto a esto, refiérase al documento **_respuestas.txt_** que también se encuentra en este repositorio.

### ¿Cómo lo calcula?
Respecto a los valores númericos, hay dos operaciones matemáticas que se realizan durante la ejecución del código:
* La primera corresponde a los cálculos que se hacen para poder imprimir _ansParcial_, la variable que se mostró en la pregunta anterior. Para esto se toma el número de unidades que el cliente va a adquirir (variable _unidades_) y se multiplica por el precio de una unidad (variable _precio_). Luego se realiza el descuento, _desc_, pertinente (que se ha asignado anteriormente de acuerdo con el _rol_).

```python
totalProducto = int(unidades * precio)
totalParcial = int(totalProducto - (totalProducto * desc))
```

  A todo esto se le realiza la operación **_int_** debido a que en Colombia no se usan valores decimales / centavos. El resultado, almacenado en _totalParcial_ es lo que se imprime en la respuesta dada por cada producto que registra el usuario.

* La segunda corresponde al total de la cuenta, después de que el cliente indica que ya no quiere registrar más productos. Cada vez que el usuario ingresa un producto, el precio de este multiplicado por las unidades (sin el descuento), se añade al total final:

```python
totalSinDesc += totalProducto
```

Luego, a esta variable _totalSinDesc_ se le realiza el descuento para obtener el total (variable _total_):

```python
total = int(totalSinDesc - (totalSinDesc * desc))
```
- - - -

Esto concluye el ReadMe de este repositorio. Gracias por leer.

- - - -
