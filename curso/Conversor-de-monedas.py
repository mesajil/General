COPXDOLAR = 3778.16

if __name__ == "__main__":
    while (1):
        pesos = float(input("Ingrese pesos colombianos: "))
        print (pesos/COPXDOLAR)
        print ("{:.2f}".format(pesos/COPXDOLAR))
        print (round(pesos/COPXDOLAR, 2))
