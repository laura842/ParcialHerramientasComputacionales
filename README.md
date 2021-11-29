# ParcialHerramientasComputacionales
### ¿Qué problema es?
El *problema* que se plantea y se busca resolver es el de realizar un programa para un sistema de descuentos en la cafetería de la Universidad Javeriana como ayuda para la situación económica de estudiantes y profesores debido a la pandemia. Este programa debe solicitar los datos del cliente, específicamente su cédula y rol dentro de la Universidad. Dependiendo de este último, el descuento será diferente: si el cliente es profesor, tendrá un 20% de descuento; si es estudiante, tendrá 50% de descuento. 

Además de esto, el programa debe requerir (en su versión inicial) el código del producto a adquirir, el precio de este y la cantidad que el cliente desea comprar. Después de ingresar esta información, el programa debe realizar los cálculos correspondientes de manera que pueda imprimir el total de la compra después de que se le ha aplicado el descuento, así como otros datos, de la siguiente forma:

> ”El **_rol_** con cédula **_número_**, debe pagar **_valor_** por el producto **_código_**”

### ¿Qué modelo computacional lo resuelve?

```python
checkFunc = input("¿Seguir registrando usuarios? (Si o No): ")

if checkFunc == "Si" or checkFunc == "Sí" or checkFunc == "SI" or checkFunc == "si" or checkFunc == "sí":
  funcionamiento = True
  ingresarProductos = True
  ans = ""
  ansParcial = ""
  totalSinDesc = 0
  print("--------------")
  ```

### ¿Qué recibe el algoritmo como entrada?
El programa recibe múltiples inputs por parte del usuario, algunos convirtiéndose a números enteros (ints) de manera que se posible operar con ellos, y otros dejándose como cadenas de texto (str):
* **integers** - precio y unidades del producto a registrar
* **strings** - cédula y rol del cliente, así como el código del producto. 
<br>
Asimismo, después de imprimir la respuesta esperada, el algoritmo recibe dos inputs más para corroborar si el cliente desea que un ciclo particular del programa siga corriendo. Uno de estos es para verificar si el usuario desea registrar más productos y el otro es para saber si hay más clientes por pasar a la caja. Estos son inputs de cadena (str) que aceptan diferentes versiones de "Si" o "No".

### ¿Cuál es la salida esperada? 
En la versión final hay dos salidas esperadas. Debido a que el cliente puede ingresar varias cantidades de productos diferentes, entonces se va creando algo similar a una cuenta en la que se muestra la cédula, el rol

```
hello world!
```

### ¿Cómo lo calcula?

```python
totalProducto = int(unidades * precio)
totalParcial = int(totalProducto - (totalProducto * desc))
```

```python
totalSinDesc += totalProducto
```
