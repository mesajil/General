from math import sqrt
def obtenerEcuacion (x):
    return sqrt(5 - x) + pow(x,2) - 5
def obtenerCuadratica (x, t):
    # Para x = 2, y t = (1, 4, 3) => x^2 + 4*x + 3 => 2^2 + 4*2 + 3 = 15
    return t[0] * pow(x,2) + t[1] * x + t[2]

x = [(-1 + sqrt(69))/4, (-1 - sqrt(69))/4]
ecuacion = (4,2,-17)
print (obtenerCuadratica(x[0], ecuacion))
print (obtenerCuadratica(x[1], ecuacion))

print (obtenerEcuacion(x[0]))
print (obtenerEcuacion(x[1]))

x = [(-1 + sqrt(21))/2, (1 - sqrt(17))/2]
print ("Solucion")
print (obtenerEcuacion(x[0]))
print (obtenerEcuacion(x[1]))

print ("Solucion alternativa 1")
x = [(-1 + sqrt(21))/2, (-1 - sqrt(21))/2]
print (obtenerEcuacion(x[0]))
print (obtenerEcuacion(x[1]))
ecuacion = (1,1,-5)
print (obtenerCuadratica(x[0], ecuacion))
print (obtenerCuadratica(x[1], ecuacion))


print ("Solucion alternativa 2")
x = [(1 + sqrt(17))/2, (1 - sqrt(17))/2]
print (obtenerEcuacion(x[0]))
print (obtenerEcuacion(x[1]))
ecuacion = (1,-1,-4)
print (obtenerCuadratica(x[0], ecuacion))
print (obtenerCuadratica(x[1], ecuacion))
