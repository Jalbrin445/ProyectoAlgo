# Proyecto Curso Algoritmos y Programación.

Este proyecto se desarrollo con el fin de dar cumplimiento al objetivo general o principal del proyecto, siendo este el siguiente: Desarrollar un prototipo funcional de una aplicación 
de escritorio que facilite el cálculo del cambio de la entalpía específica considerando algunas variables como: 
(∆°T, Presión y el tipo de sustancia) y teniendo en cuenta diferentes unidades de medida (°C o K, Pa o bar, agua (H2O) o metanol (CH4O).

Donde se definieron requisitos funcionales como:

1. Calcular la entalpía haciendo uso de la propiedad calor específico.
2. Ingresar temperatura a través de teclado.
3. Seleccionar sustancias.
4. Cambiar las unidades de Temperatura.
5. Mostrar polinomio a calcular.

Si se quiere hacer uso de la aplicación se deben instalar las siguientes dependencias:
En primer lugar, verificar si la biblioteca pip ya esta instalada, de ser así, entonces se procede a:

* pip install pandas (para datos con .xlsx).
* pip install tkinter (para interfaz).
* pip install sympy (procesamiento de integral).
* pip install pyarrow (procesamiento de datos con .xlsx (para aumentar la eficiencia en el procesamiento de datos))
* pip install pillow (procesamiento de imagenes).

Para ejecutar y utilizar la aplicación de forma correcta:
Se ejecuta el archivo main.py >> se seleciona la sustancia >> si se desean modificar las entrada de temperatura se procede o en caso contrario, se dejan como estaban>>
se selecciona la unidad de temperatura (°C) o (K) si se desea >> Se presiona el botón "Calcular Entalpía">> se abre una pestaña y se evidencian los resultados >> se cierra la aplicación o se escoge una nueva sustancia o rango de temperatura.

