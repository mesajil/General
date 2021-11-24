


"""

"""
# FILES

n_files = 6
f_title = "ventas{year}{month}.txt"

n_lines_per_file = 10

# DATA

date_ini = "16/11/2021"
max_y = 100
max_x = 100
min_y = 0
min_x = 0
max_m3 = 60
min_m3 = 5
mim_h_lim = 4
max_h_lim = 24


# PREPARE DATA

sep = ","
data=[]
data.append(date_ini)
data.append(max_y)
data.append(max_x)
data.append(max_m3)
data.append(max_h_lim)
n_data_per_line = len(data)




def enter_line (f):
    for i in range (n_data_per_line):
        f.write (str(data[i]))
        if (i+1 != n_data_per_line):
            f.write (sep)
        else:
            f.write ("\n")

def enter_data (f):

    for i in range(n_lines_per_file):
        enter_line(f)
        


def main ():



    for i in range(n_files):
        f = open (f_title.format(year="2020", month=i), "w+")
        enter_data (f)
        f.close()



if __name__ == "__main__":
    main()