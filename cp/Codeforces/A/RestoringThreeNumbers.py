""" 
Recuperar los tres números enteros positivos a, b, c
Dados los siguientes cuatro números: a + b, b + c, b + c, a + b + c
 """




numbers = list(map(int, input ().split()))

numbers.sort(reverse=True)

print (numbers[0] - numbers[1], numbers[0] - numbers[2], numbers[0] - numbers[3])