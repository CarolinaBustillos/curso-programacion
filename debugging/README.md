# Debugging

En el presente directorio, se utilizó el debugging para corregir un código para calcular y comparar un promedio.

## Errores

1. En la función comparar_con_promedio() el if, elif, y else no tienen ":" al final por lo que es un error de sintaxis.
2. Al pedir los tres números al usuario el "num" es un string (cadena de texto), pero se necesita trabajar con valores numéricos ya que se deben hacer comparaciones con <,> o =.

## Soluciones

1. Agregarle los ":" al final de la línea.
2. En este caso hay dos posibles soluciones; la primera opción es utilizar un int y trabajar con valores enteros, la segunda opción es utilizar un float que permite trabajar tanto con enteron como con decimales y por esa variedad se decidió trabajar con este último.

## Extra

1. En la función calcular_promedio() simplemente se calcula el promedio sin embargo no se le indica al usuario. Por esto se decidió agregar un total donde se calcule el promedio y luego imprimirlo para asegurarle al usuario que está bien calculado. 

## Uso del Debugging

Se utilizó el Debugging en promedio = calcular_promedio(numeros) y comparar_con_promedio(numeros, promedio) para asegurarse de que hasta esos puntos se estuviera ejecutando de manera correcta el programa, y en el momento que algo estuviera incorrecto se identificó de manera más eficiente. 