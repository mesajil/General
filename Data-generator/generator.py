
import os
import random
import datetime
import data_classes

# FILES PARAMETERS

n_files = 2
f_title = "ventas{year}{month}.txt"
n_lines_per_file = 1
dir = "output/"


# DATA PARAMETERS

a = 5
b = 24
n = 1.223
x = 1
grown_glp = data_classes.Grown_glp(a,b,n,x)
year = 2021
month = 11
day = 16
date = data_classes.Date(datetime.datetime(year, month, day))

sale_point = data_classes.Point ()
sale_m3 = data_classes.CubicMeters()
sale_dhours = data_classes.DeadLineHours()

sale_point.set_max_x(70)
sale_point.set_max_y(50)
sale_point.set_min_x(0)
sale_point.set_min_y(0)
sale_m3.set_max(60)
sale_m3.set_min(1)
sale_dhours.set_max(36)
sale_dhours.set_min(4)
sale_dhours.set_dhours(0)


# PREPARE DATA CONDITIONS

sep = ","
data=[]
data.append("16/11/2021")
data.append(0)
data.append(0)
data.append(0)
data.append(0)
n_data_per_line = len(data)

map = data_classes.Map ([(12,8)], [(42,42), (63,3)])
#map = data_classes.Map ([(1,8)], [(2,2), (6,3)])
valid_points = [(i,j) for i in range(sale_point.get_min_x(), sale_point.get_max_x() + 1) for j in range(sale_point.get_min_y(), sale_point.get_max_y() + 1) if (i,j) not in (map.main_plants+map.inter_plants)]

m3_ranges = [(1,4),(5,9),(10,14),(15,24),(25,60)]
m3_weights = [10,4,4,2,1]

time_lim_ranges = [(4,4), (5,12), (13,18), (19,36)]
time_lim_weights = [10,40,40,10]



def enter_line (f):
    
    data.insert(0, "{day}:{hour}:{minute}".format(day = date.get_date().day, hour = date.get_date().hour, minute = date.get_date().minute))
    
    point = random.choice(valid_points)
    time_lim_range = random.choices(population = time_lim_ranges, weights=time_lim_weights, k = 1)[0]
    m3_range = random.choices(population = m3_ranges, weights=m3_weights, k = 1)[0]
    glp = random.randint(m3_range[0], m3_range[1])
    data.insert(1, point[0])
    data.insert(2, point[1])
    data.insert(3, glp)
    data.insert(4, random.randint(time_lim_range[0], time_lim_range[1]))
    
    for i in range (n_data_per_line):

        f.write (str(data[i]))

        if (i+1 != n_data_per_line):
            f.write (sep)
        else:
            f.write ("\n")
    return glp

def enter_data (f):
    for i in range(2):
        glp_max_day = grown_glp.get_glp()
        grown_glp.inc_x()
        glp_day = 0
        while (glp_day < glp_max_day):
            glp_day += enter_line(f)
        date.inc_a_day()


def create_files ():

    try:
        os.mkdir(dir)
    except:
        pass

    for i in range(n_files):
        f = open ((dir+f_title).format(year="2020", month=i), "w+")
        enter_data (f)
        f.close()



if __name__ == "__main__":
    #print (valid_points)
    #print (random.choices(population = time_lim_ranges, weights=time_lim_weights, k = 1))
    create_files()