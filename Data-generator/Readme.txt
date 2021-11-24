
El archivo histórico de pedidos es mensual y tiene la siguiente estructura:

Nombre de archivo será: ventas2021mm mm=mes (01 para enero, 02 para febrero, así sucesivamente)
Registro: dd:hh:mi,posx,posY,m3, hLímite
Ejemplo: 12:08:10,65, 49, 15, 18

dd:hh:mi es el día, hora y minuto en que el pedido llegó; en el ejemplo es 12:08:10
posX,posY es la ubicación de la entrega, en el ejemplo es 65,49
m3 es la cantidad de GLP en metros cúbicos (número entero), en el ejemplo es 15
hlimite, el número de horas límite de la entrega, en el ejemplo 18.


  a. A partir de la data histórica, los equipos deben generar la data futura. En relación al punto 2, este proceso es INDEPENDIENTE de las simulaciones, pueden crear sus datos futuros las veces que sean necesarias, por lo que NO deben amarrarlo al proceso de simulación al colapso o simulación 3 días.
    b. La fecha de inició de la data futura será: el martes 16 de noviembre 2021, se sugiere que generen por, al menos, 6 meses.
    c. Los datos históricos se han generado usando una función polinomial de la forma....
             x = día de la simulación, comienza en 1, 2, ....
             y = cantidad de pedidos
             n = parámetro de crecimiento
             a, b coeficientes
       La data futura se debe generar de la misma manera.


1. Los datos históricos y datos futuros, del volumen de GLP en m3 por día (max_GLP_día), inicialmente entregados para el curso, han sido generados a partir de una función polinomial de la forma....  y = a x ^ n + b
             x = día de la simulación, comienza en 1, 2, ....
             y = volumen total de GLP para el día (x)
             n = parámetro de crecimiento
             a, b coeficientes
     En el proceso de generación de volumen de GLP, se ha usado, en varios momentos, la función random() para introducir un grado de aleatorización a la data y usado algunas reglas adicionales.

2. A continuación, voy a comentar las consideraciones seguidas para los datos proporcionados
     a.  La fórmula usada, esta vez, fue:  y = 5 * x ^ 1.223 + 240;  dicha fórmula será ajustada para los datos finales. Se les enviará los datos definitivos en unos días.
          Se generaron datos para 500 días. Se espera generar datos por 1200 días para la prueba final.
     b.  En relación a la cantidad de GLP por camión cisterna se ha usado el siguiente esquema:  
                     T+ = 1         = 4.8% (1/21)        genera de 25m3 a más
                     TA = 2         = 9.5% (2/21)        genera de 15 a menos de 25m3          
                     TB= 4         =19.05% (4/21)      genera de 10 a menos de 15m3
                     TC = 4        = 19.05 (4/21)        genera de 5 a menos de 10m3
                     TD = 10      = 47.6% (10/21)     genera de 1 a menos de 5m3
            TA, TB, TC y TD son tipos de camiones cisternas (ver preguntas y respuestas).
            T+ representa la situación de pedidos que son más grandes de los camiones TA (los de mayor capacidad de la flota).

            La determinación de la cantidad de GLP por pedido está influenciada por el tipo de camión (TA,..,TD, T+). Pero se usó una función aleatoria. 
            Se usó como restricción  max_GLP_día, por lo que en los primeros días, es posible, que no se cumpla lo del esquema (a nivel de las proporciones finales).
 
            IMPORTANTE. En su generación, si deberían considerar esta proporción para una mejor distribución del max_GLP_día
            Notar que la cantidad de pedidos está determinado por cómo se "van generando las cantidades de cada pedido" y cuya suma del día debe ser menor que el max_GLP_día. 
            IMPORTANTE. En la generación proporcionada, se ha usado funciones aleatorias. Ustedes pueden usar funciones lineales u otras, manteniendo el hecho que en el día sea igual (cercano) al max_GLP_día.

    c.  En relación a la ubicación destino de los pedidos, 
         Se ha usado una función aleatoria para distribuirlo en toda la ciudad. Solo deben tener cuidado de no coincidir con la ubicación de las plantas (central e intermedias).

     d. En relación al plazo de entrega se ha usado una función aleatoria que distribuya (aproximadamente) de la siguiente manera :
              10% en 4 horas
              40% entre 5 y 12 horas
              40% entre 12 y 18 horas
              10% entre 18 y 36 horas. 

     e. Para el horario de los pedidos, en cada día, se ha usado una fórmula que por aproximación, busca distribuirse en todo el día de manera uniforme.
         Menos notorio al principio, pero más uniforme conforme avanzan los días.

PARA EL GENERACIÓN DE DATOS (Pronóstico)
- Para los equipos de 3 estudiantes, NO deben considerar esta tarea, pues se les proveerá un juego datos de pruebas finales.
- Para los equipos de 4 estudiantes, se les sugiere, buscar esquemas sencillos que logren un efecto parecido al que se ha descrito en la sección anterior.

IMPORTANTE. En la simulación
- Lo que deberían considerar para iniciar la simulación (3 días o de colapso logístico) es que se coloque una fecha-hora de inicio de la simulación (ejecución del algoritmo o un efecto similar).
- A partir de esa fecha-hora, se inicia el consumo de datos de los pedidos. Se asume que no hay pedidos anteriores. Entonces, si se ejecuta el algoritmo en ese momento, no se genera ninguna ruta.
  Para la siguiente ejecución, aplica todo lo comentado en el video al respecto.