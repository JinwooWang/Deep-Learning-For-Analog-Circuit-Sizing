import os
from math import fabs
import csv

def get_gbw_and_ADC():
    l = os.listdir("./src/bandwidth/output")
    phi_dic = {}
    for filename in l:
        minus_start = 0
        minus_end = 0
        fcontent = open("./src/bandwidth/output/%s"%(filename), "r").readlines()
        fwrite = open("./src/bandwidth/ADC_GBW/%s.out"%(filename[:-4]), "w")
        k = 0
        flag_m = 0
        flag_init = 0
        db_list = []
        freq_list = []
        for line in fcontent:
            splited_line = line.split()
            #print splited_line
            k += 1
            if splited_line != [] and splited_line[0] == "frequency":
                freqk = k
                continue
            if len(splited_line) > 2:

                if splited_line[0] != '' and splited_line[0][0] == "1" and flag_init == 0:
                    flag_init = 1
                    if(float(splited_line[1]) < 40):
                        print filename
                        os.remove("./src/bandwidth/output/%s"%(filename))
                        os.remove("./src/bandwidth/input/%s.sp"%(filename[:-4]))
                        os.remove("./src/bandwidth/ADC_GBW/%s.out"%(filename[:-4]))
                        name = filename[:-4]
                        #print name
                        os.remove("./src/phase/output/opamp_phase_%s.log"%(name[16:]))
                        os.remove("./src/phase/input/opamp_phase_%s.sp"%(name[16:]))
                        os.remove("./src/CMRR/output/opamp_CMRR_%s.log"%(name[16:]))
                        os.remove("./src/CMRR/input/opamp_CMRR_%s.sp"%(name[16:]))
                        os.remove("./src/PSRR/output/opamp_PSRR_%s.log"%(name[16:]))
                        os.remove("./src/PSRR/input/opamp_PSRR_%s.sp"%(name[16:]))

                        break
                    #freq_list.append(float(splited_line[0]))
                    #db_list.append(float(splited_line[1]))
                    fwrite.write(str(float(splited_line[1])))
                    fwrite.write(" ")
                    continue

                if splited_line[1] != '' and splited_line[1][0] == "-" and splited_line[1][2:6] != "----" and flag_m == 0:
                    flag_m = 1
                    #fwrite.write(splited_line[1])
                    #fwrite.write(" ")
                    fwrite.write(str(float(splited_line[0])))
                    fwrite.write(" ")
                    #freq_list.append(float(splited_line[0]))
                    #db_list.append(float(splited_line[1]))
                    m_freq = float(splited_line[0])
                    m_db = float(splited_line[1])
                    minus_end = k + 10
                    minus_start = k

                if minus_start < k < minus_end:
                    #fwrite.write(splited_line[1])
                    p_ind = 2*minus_start - k - 1
                    if k == minus_start + 1:
                        p_freq = float(fcontent[p_ind].split()[0])
                        p_db = float(fcontent[p_ind].split()[1])

        if fabs(m_db) < fabs(p_db):
            phi_dic[filename[-5]] = m_freq
        else:
            phi_dic[filename[-5]] = p_freq

        fwrite.close()
    return phi_dic

def get_phase_margin(phi_dic):
    print phi_dic
    l = os.listdir("./src/phase/output")
    for filename in l:
        minus_start = 0
        minus_end = 0
        fcontent = open("./src/phase/output/%s"%(filename), "r").readlines()
        fwrite = open("./src/phase/PM/%s.out"%(filename[:-4]), "w")
        phi_key = filename[-5]
        phi_list = []
        freq_list = []
        flag_m = 0
        k = 0
        for line in fcontent:
            splited_line = line.split()
            #print splited_line
            k += 1
            if splited_line != [] and splited_line[0] == "frequency":
                freqk = k
                continue
            if len(splited_line) > 2:
                if len(splited_line[0]) > 4:
                    if splited_line[0][-3] == "+" and float(splited_line[0]) == phi_dic[phi_key] and flag_m == 0:
                        print phi_dic[phi_key]
                        print "============"
                        flag_m = 1
                        freq_list.append(float(splited_line[0]))
                        phi_list.append(float(splited_line[1]))
                        PM = float(180.0 - fabs(57.29577*float(splited_line[1])))

                        minus_end = k + 10
                        minus_start = k

                    if minus_start < k < minus_end:
                        p_ind = 2*minus_start - k - 1
                        freq_list.append(float(splited_line[0]))
                        phi_list.append(float(splited_line[1]))
                        freq_list.append(float(fcontent[p_ind].split()[0]))
                        phi_list.append(float(fcontent[p_ind].split()[1]))
        #print phi_list

        L = zip(freq_list, phi_list)
        L.sort(lambda x, y:cmp(x[0],y[0]))
        #print L
        j =0
        for (freq, phi) in L:
            #freq_list[j] = freq
            phi_list[j] = phi
            j += 1


        fwrite.write(str(PM))
        fwrite.close()

def get_CMRR():
    l = os.listdir("./src/CMRR/output")
    phi_dic = {}
    for filename in l:
        minus_start = 0
        minus_end = 0
        fcontent = open("./src/CMRR/output/%s"%(filename), "r").readlines()
        fwrite = open("./src/CMRR/cmrr/%s.out"%(filename[:-4]), "w")
        k = 0
        flag_m = 0
        flag_init = 0
        db_list = []
        freq_list = []
        for line in fcontent:
            splited_line = line.split()
            #print splited_line
            k += 1
            if splited_line != [] and splited_line[0] == "frequency":
                freqk = k
                continue
            if len(splited_line) > 2:

                if splited_line[0] != '' and splited_line[0][0] == "1" and flag_init == 0:
                    flag_init = 1
                    #freq_list.append(float(splited_line[0]))
                    #db_list.append(float(splited_line[1]))
                    fwrite.write(str(float(splited_line[1])))
                    fwrite.write(" ")
                    continue

        fwrite.close()

def get_PSRR():
    l = os.listdir("./src/PSRR/output")
    phi_dic = {}
    for filename in l:
        minus_start = 0
        minus_end = 0
        fcontent = open("./src/PSRR/output/%s"%(filename), "r").readlines()
        fwrite = open("./src/PSRR/psrr/%s.out"%(filename[:-4]), "w")
        k = 0
        flag_m = 0
        flag_init = 0
        db_list = []
        freq_list = []
        for line in fcontent:
            splited_line = line.split()
            #print splited_line
            k += 1
            if splited_line != [] and splited_line[0] == "frequency":
                freqk = k
                continue
            if len(splited_line) > 2:

                if splited_line[0] != '' and splited_line[0][0] == "1" and flag_init == 0:
                    flag_init = 1
                    #freq_list.append(float(splited_line[0]))
                    #db_list.append(float(splited_line[1]))
                    fwrite.write(str(float(splited_line[1])))
                    fwrite.write(" ")
                    continue

        fwrite.close()

#ADC GBW PM
def input_csv_generation():
    path1 = "./src/bandwidth/ADC_GBW/"
    path2 = "./src/phase/PM/"
    path3 = "./src/CMRR/cmrr/"
    path4 = "./src/PSRR/psrr/"
    l1 = os.listdir(path1)
    l2 = os.listdir(path2)
    l3 = os.listdir(path3)
    l4 = os.listdir(path4)
    outfile = open("./csv/norm_dataset.csv", "w")
    csv_write = csv.writer(outfile, dialect = "excel")
    filedic = {}
    for filename1 in l1:
        name = filename1[:-4]
        filedic[int(name[16:])] = filename1
    for filename2 in l2:
        name = filename2[:-4]
        filename1 = filedic[int(name[12:])]
        filedic[int(name[12:])] = [filename1, filename2]
    for filename3 in l3:
        name = filename3[:-4]
        #print filedic[int(name[11:])]
        filename1, filename2 = filedic[int(name[11:])]
        filedic[int(name[11:])] = [filename1, filename2, filename3]
    for filename4 in l4:
        name = filename4[:-4]
        filename1, filename2, filename3 = filedic[int(name[11:])]
        filedic[int(name[11:])] = [filename1, filename2, filename3, filename4]


    sorted(filedic.keys())
    for item in filedic:
        #print filedic[item]
        filename1, filename2, filename3,filename4 = filedic[item]
        fcontent1 = open(path1 + filename1, "r").readline()
        fcontent1_splited = fcontent1.split()
        fcontent2 = open(path2 + filename2, "r").readline()
        fcontent2_splited = fcontent2.split()
        fcontent3 = open(path3 + filename3, "r").readline()
        fcontent3_splited = fcontent3.split()
        fcontent4 = open(path4 + filename4, "r").readline()
        fcontent4_splited = fcontent4.split()
        fcontent1_splited.append(fcontent2_splited[0])
        fcontent1_splited.append(fcontent3_splited[0])
        fcontent1_splited.append(fcontent4_splited[0])
        csv_write.writerow(fcontent1_splited)

    outfile.close()
    return filedic

def output_csv_generation(filedic):
    path1 = "./src/bandwidth/input/"
    l1 = os.listdir(path1)
    outfile = open("./csv/w_l_dataset.csv", "w")
    csv_write = csv.writer(outfile, dialect = "excel")
    for item in filedic:
        witem = []
        filename1 = filedic[item][0][:-4] + ".sp"
        fcontent = open(path1 + filename1, "r").readlines()
        for line in fcontent:
            if line[0] == "m":
                splited_line = line.split()
                if line[1] == '3' or line[1] == '5':
                    continue
                for ind in splited_line:
                    if ind[0] == "w":
                        witem.append(ind[2:-1])
                    elif ind[0] == "l":
                        witem.append(ind[2:-1])
        csv_write.writerow(witem)
    outfile.close()

if __name__ == "__main__":
    phi_dic = get_gbw_and_ADC()
    get_phase_margin(phi_dic)
    get_CMRR()
    get_PSRR()
    filedic = input_csv_generation()
    output_csv_generation(filedic)
