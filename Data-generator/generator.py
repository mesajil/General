
import os
import random
import datetime
import data_classes
import calendar

# FILES PARAMETERS

n_files = 9
f_title = "ventas{year}{month}.txt"
n_lines_per_file = 1
dir = "output/"


# DATA PARAMETERS

a = 5
b = 240
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


map = data_classes.Map ([(12,8)], [(42,42), (63,3)])
#map = data_classes.Map ([(1,8)], [(2,2), (6,3)])
valid_points = [(i,j) for i in range(sale_point.get_min_x(), sale_point.get_max_x() + 1) for j in range(sale_point.get_min_y(), sale_point.get_max_y() + 1) if (i,j) not in (map.main_plants+map.inter_plants)]

m3_ranges = [(1,4),(5,9),(10,14),(15,24),(25,60)]
m3_weights = [10,4,4,2,1]

time_lim_ranges = [(4,4), (5,12), (13,18), (19,36)]
time_lim_weights = [10,40,40,10]





def set_date (data_file):
    format_date = "{day%2}:{hour%2}:{minute%2}"
    step_seconds = int(24*60*60/len(data_file.get_data()))
    rand_second = random.randint(0, step_seconds - 1)
    date_line = datetime.datetime(date.get_date().year,date.get_date().month,date.get_date().day)
    date_line += datetime.timedelta(seconds = rand_second)
    for data in data_file.get_data():
        data.insert(0, date_line.strftime("%d:%H:%M"))
        date_line += datetime.timedelta(seconds = step_seconds)
        
def enter_line (data_lines):
    
    
    point = random.choice(valid_points)
    time_lim_range = random.choices(population = time_lim_ranges, weights=time_lim_weights, k = 1)[0]
    time_lim = random.randint(time_lim_range[0], time_lim_range[1])
    m3_range = random.choices(population = m3_ranges, weights=m3_weights, k = 1)[0]
    glp = random.randint(m3_range[0], m3_range[1])

    line = data_classes.Data ()
    line.set_data ([point[0], point[1], glp, time_lim])
    data_lines.add (line.get_data())
    return glp

def get_data ():
    data_file = data_classes.Data()
    for i in range(calendar.monthrange(date.get_date().year, date.get_date().month)[1] - date.get_date().day + 1):
        data_lines = data_classes.Data()
        glp_max_day = grown_glp.get_glp()
        grown_glp.inc_x()
        glp_day = 0
        while (glp_day < glp_max_day):
            glp_day += enter_line(data_lines)
        set_date (data_lines)
        data_lines = [",".join([str(e) for e in data]) for data in data_lines.get_data()]
        data_file.add("\n".join(data_lines))
        date.inc_a_day()
    return data_file.get_str_data("\n")



def generate_data ():

    try:
        os.mkdir(dir)
    except:
        pass

    for i in range(n_files):
        f = open (dir+"ventas"+date.get_date().strftime("%Y%m")+".txt", "w")
        f.write (get_data ())
        f.close()



if __name__ == "__main__":

    generate_data()