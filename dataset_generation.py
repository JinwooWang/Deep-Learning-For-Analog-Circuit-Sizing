import random

file_list = ["opamp_bandwidth.sp", "opamp_phase.sp", "opamp_CMRR.sp", "opamp_PSRR.sp"]
folder_list = ["bandwidth", "phase", "CMRR", "PSRR"]
"""
M1_list = [5]
M4_list = [5, 45]
M7_list = [70, 75, 80]
M8_list = [12]
"""

M1_list = [5]
M4_list = [5, 20, 45]
M7_list = [70, 80, 90]
M8_list = [12.7]

def generate_spfile():

    for i in range(20000):
        restore_wm = random.randint(10500, 19500)
        #restore_lm = random.randint(250, 1200)
        restore_lm = 1000
        restore_wd = random.randint(3500, 6500)
        #restore_ld = random.randint(250, 1200)
        restore_ld = 1000
        mos_dic = {}
        mos_ldic = {}
        mos_wdic = {}
        k = 0
        for filename in file_list:
            fcontent = open("./cir_file/%s"%(filename), "r").readlines()
            fwrite = open("./src/%s/input/%s_%d.sp"%(folder_list[k], filename[:-3], i), "w")
            for line in fcontent:
                if line[0] == "m":
                    new_line = ""
                    splited_line = line.split(" ")
                    if line[1] == "1":
                        for item in splited_line:
                            if item[0] == "w":
                                w1 = random.randint(3150, 5850)
                                item = "w=%dn"%(w1)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "2":
                        for item in splited_line:
                            if item[0] == "w":

                                item = "w=%dn"%(restore_wm)
                            elif item[0] == "l":

                                item = "l=%dn"%(restore_lm)
                            new_line += item
                            new_line += " "
                    elif line[1] == "3":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(restore_wm)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_lm)
                            new_line += item
                            new_line += " "
                    elif line[1] == "4":
                        for item in splited_line:
                            if item[0] == "w":

                                item = "w=%dn"%(restore_wd)
                            elif item[0] == "l":

                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "5":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(restore_wd)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "

                    elif line[1] == "6":
                        for item in splited_line:
                            if item[0] == "w":
                                w6 = random.randint(3150, 5850)
                                item = "w=%dn"%(w6)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "7":
                        for item in splited_line:
                            if item[0] == "w":
                                w7 = random.randint(65800, 122200)
                                item = "w=%dn"%(w7)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "8":
                        for item in splited_line:
                            if item[0] == "w":
                                w8 = random.randint(9800, 18200)
                                item = "w=%dn"%(w8)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    new_line += "\n"
                    fwrite.write(new_line)
                else:
                    fwrite.write(line)
            fwrite.close()
            k += 1

def generate_spfile_knowledge(num_start, num_to_generate, mlist):

    for i in range(num_start, num_to_generate):
        restore_wm = random.randint(15000 * 0.95, 15000 * 1.05)
        #restore_lm = random.randint(250, 1200)
        restore_lm = 1000
        restore_wd = random.randint(mlist[1]*950, mlist[1]*1050)
        #restore_ld = random.randint(250, 1200)
        restore_ld = 1000
        mos_dic = {}
        mos_ldic = {}
        mos_wdic = {}
        k = 0
        w1 = random.randint(mlist[0]*950, mlist[0]*1050)
        w8 = random.randint(mlist[3]*950, mlist[3]*1050)
        w6 = random.randint(4500*0.95, 4500*1.05)
        w7 = random.randint(mlist[2]*950, mlist[2]*1050)
        for filename in file_list:
            fcontent = open("./cir_file/%s"%(filename), "r").readlines()
            fwrite = open("./src/%s/input/%s_%d.sp"%(folder_list[k], filename[:-3], i), "w")
            for line in fcontent:
                if line[0] == "m":
                    new_line = ""
                    splited_line = line.split(" ")
                    if line[1] == "1":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(w1)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "2":
                        for item in splited_line:
                            if item[0] == "w":

                                item = "w=%dn"%(restore_wm)
                            elif item[0] == "l":

                                item = "l=%dn"%(restore_lm)
                            new_line += item
                            new_line += " "
                    elif line[1] == "3":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(restore_wm)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_lm)
                            new_line += item
                            new_line += " "
                    elif line[1] == "4":
                        for item in splited_line:
                            if item[0] == "w":

                                item = "w=%dn"%(restore_wd)
                            elif item[0] == "l":

                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "5":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(restore_wd)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "

                    elif line[1] == "6":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(w6)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "7":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(w7)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    elif line[1] == "8":
                        for item in splited_line:
                            if item[0] == "w":
                                item = "w=%dn"%(w8)
                            elif item[0] == "l":
                                item = "l=%dn"%(restore_ld)
                            new_line += item
                            new_line += " "
                    new_line += "\n"
                    fwrite.write(new_line)
                else:
                    fwrite.write(line)
            fwrite.close()
            k += 1

def generate_sp(spnum):
    mos_list = []
    for m1 in M1_list:
        for m4 in M4_list:
            for m7 in M7_list:
                for m8 in M8_list:
                    mos_list.append([m1, m4, m7, m8])
    cor_num = len(mos_list)
    per_cor_num = spnum/cor_num
    counter = 0
    for i in range(spnum):
        if counter != cor_num - 1:
            if i % per_cor_num == 0:
                generate_spfile_knowledge(i, i + per_cor_num, mos_list[counter])
                counter += 1
        else:
            generate_spfile_knowledge(i, spnum, mos_list[counter])

if __name__ == "__main__":
    generate_sp(9000)
