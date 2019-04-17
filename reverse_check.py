import csv
import os
from math import fabs

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

def tmpsp_generation(wl_list):
    infile1 = open("./src/bandwidth/input/opamp_bandwidth_0.sp", "r").readlines()
    infile2 = open("./src/phase/input/opamp_phase_0.sp", "r").readlines()
    infile3 = open("./src/CMRR/input/opamp_CMRR_0.sp", "r").readlines()
    infile4 = open("./src/PSRR/input/opamp_PSRR_0.sp", "r").readlines()
    outfile1 = open("./tmp/input/opamp_bandwidth_tmp.sp", "w")
    outfile2 = open("./tmp/input/opamp_phase_tmp.sp", "w")
    outfile3 = open("./tmp/input/opamp_CMRR_tmp.sp", "w")
    outfile4 = open("./tmp/input/opamp_PSRR_tmp.sp", "w")
    change_wl(wl_list, infile1, outfile1)
    change_wl(wl_list, infile2, outfile2)
    change_wl(wl_list, infile3, outfile3)
    change_wl(wl_list, infile4, outfile4)

def tmplog_generation():
    os.system("ngspice -b -o ./tmp/output/opamp_bandwidth_tmp.log ./tmp/input/opamp_bandwidth_tmp.sp")
    os.system("ngspice -b -o ./tmp/output/opamp_phase_tmp.log ./tmp/input/opamp_phase_tmp.sp")
    os.system("ngspice -b -o ./tmp/output/opamp_CMRR_tmp.log ./tmp/input/opamp_CMRR_tmp.sp")
    os.system("ngspice -b -o ./tmp/output/opamp_PSRR_tmp.log ./tmp/input/opamp_PSRR_tmp.sp")

def _ADC_GBW():
    fcontent = open("./tmp/output/opamp_bandwidth_tmp.log", "r").readlines()
    k = 0
    flag_init = 0
    flag_m = 0
    minus_start = 0
    minus_end = 0
    store_list = []
    for line in fcontent:
        #if line[3:7] == "----":
            #k -= 5
        splited_line = line.split()
        k += 1
        if splited_line != [] and splited_line[0] == "frequency":
            freqk = k
            continue
        if len(splited_line) > 2:
            if splited_line[0] != '' and splited_line[0][0] == '1' and flag_init == 0:
                flag_init = 1
                """
                if(float(splited_line[1]) < 0):
                    #print filename
                    os.remove("./tmp/output/opamp_bandwidth_tmp.log")
                    os.remove("./tmp/input/opamp_bandwidth_tmp.sp")
                    os.remove("./tmp/output/opamp_phase_tmp.log")
                    os.remove("./tmp/input/opamp_phase_tmp.sp")
                    os.remove("./tmp/output/opamp_CMRR_tmp.log")
                    os.remove("./tmp/input/opamp_CMRR_tmp.sp")
                    os.remove("./tmp/output/opamp_PSRR_tmp.log")
                    os.remove("./tmp/input/opamp_PSRR_tmp.sp")

                    return -1
                """
                store_list.append(float(splited_line[1]))
                continue
            if splited_line[1] != '' and splited_line[1][0] == '-' and splited_line[1][2:6] != "----" and flag_m == 0:
                flag_m = 1
                #print k
                #print "====="
                store_list.append(float(splited_line[0]))
                m_freq = float(splited_line[0])
                m_db = float(splited_line[1])
                minus_end = k + 10
                minus_start = k
                #print minus_start
                #print "+++++++"
            #print k
            if minus_start < k < minus_end:
                p_ind = 2*minus_start - k - 1
                #print k
                #print minus_start
                #print line
                if k == minus_start + 1:
                    #if fcontent[p_ind - 1].split()[0] == "frequency":
                        #p_ind += 1
                    #if fcontent[p_ind + 1].split()[0] == "frequency":
                        #p_ind -= 1
                    p_freq = float(fcontent[p_ind].split()[0])
                    p_db = float(fcontent[p_ind].split()[1])
    if fabs(m_db) < fabs(p_db):
        phi = m_freq
    else:
        phi = p_freq
    return store_list, phi

def _PM(phi):
    fcontent = open("./tmp/output/opamp_phase_tmp.log", "r").readlines()
    k = 0
    flag_m = 0
    for line in fcontent:
        splited_line = line.split()
        k += 1
        if splited_line != [] and splited_line[0] == "frequency":
            freqk = k
            continue
        if len(splited_line) > 2:
            if len(splited_line[0]) > 4:
                if splited_line[0][-3] == "+" and float(splited_line[0]) == phi and flag_m == 0:
                    #print phi
                    #print "========="
                    flag_m = 1
                    PM = float(180.0 - fabs(57.29577*float(splited_line[1])))
                    break
    return PM

def _CMRR():
    fcontent = open("./tmp/output/opamp_CMRR_tmp.log", "r").readlines()
    k = 0
    flag_init = 0
    for line in fcontent:
        splited_line = line.split()
        k += 1
        if splited_line != [] and splited_line[0] == "frequency":
            freqk = k
            continue
        if len(splited_line) > 2:
            if splited_line[0] != '' and splited_line[0][0] == "1" and flag_init == 0:
                flag_init = 1
                return float(splited_line[1])

def _PSRR():
    fcontent = open("./tmp/output/opamp_PSRR_tmp.log", "r").readlines()
    k = 0
    flag_init = 0
    for line in fcontent:
        splited_line = line.split()
        k += 1
        if splited_line != [] and splited_line[0] == "frequency":
            freqk = k
            continue
        if len(splited_line) > 2:
            if splited_line[0] != '' and splited_line[0][0] == "1" and flag_init == 0:
                flag_init = 1
                return float(splited_line[1])

def get_tmpnorm(wl_list):
    tmpsp_generation(wl_list)
    tmplog_generation()
    store_list, freq = _ADC_GBW()
    #print store_list
    ADC = store_list[0]
    GBW = store_list[1]
    PM = _PM(freq)
    CMRR = _CMRR()
    PSRR = _PSRR()
    return ADC, GBW, PM, CMRR, PSRR


def reverse_check():
    fopen = open("./check/DNN_tst/wl_dnn.csv", "r").readlines()
    outfile = open("./check/DNN_tst/norm_out_dnn.csv", "w")
    csv_write = csv.writer(outfile, dialect = "excel")
    i = 0
    for line in fopen:
        """
        i += 1
        if i == 1:
            continue
        """
        wl_list = []
        splited_line = line.split(",")
        #print splited_line
        for ind in splited_line[:]:
            wl_list.append(float(ind))
        #print wl_list
        ADC, GBW, PM, CMRR, PSRR = get_tmpnorm(wl_list)
        norm_list = [ADC, GBW, PM, CMRR, PSRR]
        #print norm_list
        csv_write.writerow(norm_list)
    outfile.close()

def reverse_check_2():
    fopen = open("./check/RNN_tst/wl_rnn.csv", "r").readlines()
    outfile = open("./check/RNN_tst/norm_out_rnn.csv", "w")
    csv_write = csv.writer(outfile, dialect = "excel")

    for line in fopen:

        wl_list = []
        splited_line = line.split(",")
        #print splited_line
        for ind in splited_line:
            wl_list.append(float(ind))
        ADC, GBW, PM, CMRR, PSRR = get_tmpnorm(wl_list)
        norm_list = [ADC, GBW, PM, CMRR, PSRR]
        #print norm_list
        csv_write.writerow(norm_list)
    outfile.close()



if __name__ == "__main__":
    reverse_check_2()
    #store_list, freq = _ADC_GBW()
