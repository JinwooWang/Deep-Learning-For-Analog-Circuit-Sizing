import os
from math import fabs

file_list = ["opamp_bandwidth.sp", "opamp_CMRR.sp", "opamp_PSRR.sp"]
folder_list = ["bandwidth_phase", "CMRR", "PSRR"]
M1_list = [5]
M2_list = [15]
M4_list = [20, 45]
M6_list = [4.5]
M7_list = [70, 80, 90]
M8_list = [12.7]

def change_wl(wl_list, infile, outfile):
    for line in infile:
        if line[0] == "m":
            splited_line = line.split()
            if line[1] == '2' or line[1] == '3':
                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[1]*1000)

            elif line[1] == '4' or line[1] == '5':
                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[2]*1000)

            elif line[1] == '1':
                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[0]*1000)

            elif line[1] == '6':
                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[3]*1000)

            elif line[1] == '7':
                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[4]*1000)

            elif line[1] == '8':

                for k in range(len(splited_line)):
                    if splited_line[k][0] == "w":
                        splited_line[k] = "w=%sn"%(wl_list[5]*1000)

            line = ''
            for ind in splited_line:
                line += ind
                line += ' '
            line += "\r\n"
        outfile.write(line)
    outfile.close()

def sp_generation():
    wl_list_all = []
    for m1 in M1_list:
        item_list = []
        item_list.append(m1)
        for m2 in M2_list:
            item_list.append(m2)
            for m4 in M4_list:
                item_list.append(m4)
                for m6 in M6_list:
                    item_list.append(m6)
                    for m7 in M7_list:
                        item_list.append(m7)
                        for m8 in M8_list:
                            item_list.append(m8)
                            wl_list_all.append(item_list)
    i = 0
    for wl_item in wl_list_all:
        k = 0
        for filename in file_list:
            fcontent = open("./cir_file/sat/%s"%(filename), "r").readlines()
            fwrite = open("./sat_src/%s/input/%s_%d.sp"%(folder_list[k], filename[:-3], i), "w")
            change_wl(wl_item, fcontent, fwrite)
            k += 1
        i += 1

def running_ng():
    for i in range(3):
        file_list = os.listdir("./sat_src/" + folder_list[i] + "/input/")
        for filename in file_list:
            if filename[-2:] == "sp":
                path = "./sat_src/" + folder_list[i] + "/input/" + filename
                output_path = "./sat_src/" + folder_list[i] + "/output/" + filename[:-3]
                #print path
                os.system("ngspice -b -o %s.log %s"%(output_path, path))

def check_sat():
    for j in range(3):
        file_list = os.listdir("./sat_src/" + folder_list[j] + "/output/")
        for filename in file_list:
            fname = "./sat_src/%s/output/%s"%(folder_list[j], filename)
            fcontent = open("./sat_src/%s/output/%s"%(folder_list[j], filename), "r").readlines()
            i = 0
            for line in fcontent:
                splited_line = line.split()
                if len(splited_line) == 3 and splited_line[2] == "v(2)":
                    v2_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(3)":
                    v3_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(4)":
                    v4_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(5)":
                    v5_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(6)":
                    v6_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(7)":
                    v7_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(8)":
                    v8_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(9)":
                    v9_line = i + 2
                if len(splited_line) == 3 and splited_line[2] == "v(10)":
                    v10_line = i + 2
                i += 1
            v2 = float(fcontent[v2_line].split()[-1])
            v3 = float(fcontent[v3_line].split()[-1])
            v4 = float(fcontent[v4_line].split()[-1])
            v5 = float(fcontent[v5_line].split()[-1])
            v6 = float(fcontent[v6_line].split()[-1])
            v7 = float(fcontent[v7_line].split()[-1])
            v8 = float(fcontent[v8_line].split()[-1])
            v9 = float(fcontent[v9_line].split()[-1])
            v10 = float(fcontent[v10_line].split()[-1])
            flag = []
            for i in range(11):
                flag.append(0)
            if (v2 - v10) > 0.7:
                flag[0] = 1
            if fabs(v4 - 2.5) > 0.7:
                flag[1] = 1
            if fabs(v5 - 2.5) > (fabs(v4 - 2.5) - 0.7):
                flag[2] = 1
            if (v8 - v3) > 0.7:
                flag[3] = 1
            if (v4 > (v8 - 0.7)):
                flag[4] = 1
            if (v9 - v3) > 0.7:
                flag[5] = 1
            if (v5 > (v9 - 0.7)):
                flag[6] = 1
            if (v3 > (v2 - 0.7)):
                flag[7] = 1
            if fabs(v5 - 2.5) > 0.7:
                flag[8] = 1
            if fabs(v7 - 2.5) > (fabs(v5 - 2.5) - 0.7):
                flag[9] = 1
            if v7 > (v2 - 0.7):
                flag[10] = 1
            _sum = 0
            for item in flag:
                _sum += item
            if _sum != 11:
                print flag
                print "./sat_src/%s/output/%s"%(folder_list[j], filename)


if __name__ == "__main__":
    sp_generation()
    running_ng()
    check_sat()
