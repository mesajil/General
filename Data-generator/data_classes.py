import datetime

class Plant:
    x = 0
    y = 0
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def set_x (self, x):
        self.x = x
    def set_y (self, y):
        self.y = y

    def get_x (self):
        return self.x
    def get_y (self):
        return self.y

class Map:
    main_plants = []
    inter_plants = []

    def __init__ (self, main_plants, inter_plants):
        self.main_plants = main_plants
        self.inter_plants = inter_plants



class Point:

    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_max_x(self, x):
        self.max_x = x
    def set_max_y(self, y):
        self.max_y = y
    def set_min_x(self, x):
        self.min_x = x
    def set_min_y(self, y):
        self.min_y = y


    def get_x (self):
        return self.x
    def get_y (self):
        return self.y
    def get_max_x (self):
        return self.max_x
    def get_max_y (self):
        return self.max_y
    def get_min_x (self):
        return self.min_x
    def get_min_y (self):
        return self.min_y


class CubicMeters:

    def set_max (self, m3):
        self.max = m3

    def set_min (self, m3):
        self.min = m3

    def set_m3 (self, m3):
        self.m3 = m3


    def get_max (self):
        return self.max

    def get_min (self):
        return self.min
        
    def get_m3 (self):
        return self.m3


class DeadLineHours:

    def set_max (self, dhours):
        self.max = dhours

    def set_min (self, dhours):
        self.min = dhours

    def set_dhours (self, dhours):
        self.dhours = dhours


    def get_max (self):
        return self.max

    def get_min (self):
        return self.min
        
    def get_dhours (self):
        return self.dhours


class Grown_glp ():

    def __init__(self,a,b,n,x):
        self.a = a
        self.b = b
        self.n = n
        self.x = x
    
    def inc_x(self):
        self.x += 1

    def get_glp(self):
        return int ((self.a)*(self.x**self.n) + self.b)


class Date ():

    def __init__(self, date):
        self.date = date


    def inc_a_day(self):
        self.date += datetime.timedelta(days=1)
    def get_date(self):
        return self.date




        


class Data:

    def __init__(self) :
        self.data = []

    def add (self, data):
        self.data.append (data)

    def extend (self, data):
        self.data.extend(data)
    def set_data (self, data):
        self.data = data
    def get_data (self):
        return self.data
    def insert (self, index, data):
        self.data.insert (index, data)
    
    def get_str_data (self, sep):
        
        return sep.join([str(e) for e in self.data])
    

