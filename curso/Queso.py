class Queso:
    def __init__(self, hoyos):
        self.__hoyos = hoyos
    

    def get_hoyos (self):
        return self.__hoyos
    
    def set_hoyos (self, hoyos):
        self.__hoyos = hoyos


if __name__ == "__main__":
    q = Queso(5)
    print (q.get_hoyos())
    print (__name__)