import numpy as np
import matplotlib.pyplot as plt

def acc_cal():
    infile1 = open("./csv_plot/norm_out_dnn.csv", "r").readlines()
    infile2 = open("./csv_plot/norm_dataset.csv", "r").readlines()
    infile3 = open("./csv_plot/norm_out_rnn.csv", "r").readlines()
    infile4 = open("./csv_plot/wl_rnn.csv", "r").readlines()
    infile5 = open("./csv_plot/wl_dataset.csv", "r").readlines()
    infile6 = open("./csv_plot/wl_dnn.csv", "r").readlines()
    out_list = []
    truth_list = []
    out_list_rnn = []

    rnn_wl = []
    real_wl = []
    dnn_wl = []

    for line in infile4:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        rnn_wl.append(ept_list[2])
    rnn_wl = np.asarray(rnn_wl)

    for line in infile6:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        dnn_wl.append(ept_list[2])
    dnn_wl = np.asarray(dnn_wl)

    for line in infile5:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        real_wl.append(ept_list[4]/1000.0)
    real_wl = np.asarray(real_wl)

    for line in infile1:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        out_list.append(ept_list)
    out_list = np.asarray(out_list)

    for line in infile3:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        out_list_rnn.append(ept_list)
    out_list_rnn = np.asarray(out_list_rnn)

    for line in infile2:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        truth_list.append(ept_list)
    truth_list = np.asarray(truth_list)
    num = 0
    j = 0
    init_list = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0], dtype = np.float64)
    init_list_rnn = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0], dtype = np.float64)
    ADC_err_list = []
    GBW_err_list = []
    PM_err_list = []
    CMRR_err_list = []
    PSRR_err_list = []
    ADC_pred_list = []
    ADC_truth_list = []
    GBW_pred_list = []
    GBW_truth_list = []
    PM_pred_list = []
    PM_truth_list = []
    CMRR_pred_list = []
    CMRR_truth_list = []
    PSRR_pred_list = []
    PSRR_truth_list = []
    
    ADC_err_list_rnn = []
    GBW_err_list_rnn = []
    PM_err_list_rnn = []
    CMRR_err_list_rnn = []
    PSRR_err_list_rnn = []
    ADC_pred_list_rnn = []
    GBW_pred_list_rnn = []
    #GBW_truth_list = []
    PM_pred_list_rnn = []
    #PM_truth_list = []
    CMRR_pred_list_rnn = []
    #CMRR_truth_list = []
    PSRR_pred_list_rnn = []
    #PSRR_truth_list = []
    for (item1, item2) in zip(out_list, truth_list):
        j += 1
        err_list = np.fabs(item1 - item2)/item2
        flag = 0
        init_list += err_list
        ADC_err_list.append(err_list[0])
        GBW_err_list.append(err_list[1])
        PM_err_list.append(err_list[2])
        CMRR_err_list.append(err_list[3])
        PSRR_err_list.append(err_list[4])

        ADC_pred_list.append(item1[0])
        GBW_pred_list.append(item1[1])
        PM_pred_list.append(item1[2])
        CMRR_pred_list.append(item1[3])
        PSRR_pred_list.append(item1[4])

        ADC_truth_list.append(item2[0])
        GBW_truth_list.append(item2[1])
        PM_truth_list.append(item2[2])
        CMRR_truth_list.append(item2[3])
        PSRR_truth_list.append(item2[4])
        """
        for ind in acc_list:
            if ind < 0.3:
                continue
            else:
                flag = 1
                break
        if flag == 1:
            print "=================="
            print acc_list
            print item1
            print item2
            print j
            print "================="
            num += 1
        """
    err_out_list = init_list/len(out_list)
    match_out_list = np.asarray([1., 1., 1., 1., 1.])- err_out_list
    print match_out_list
    print np.mean(match_out_list)

    for (item1, item2) in zip(out_list_rnn, truth_list):
        j += 1
        err_list = np.fabs(item1 - item2)/item2
        flag = 0
        init_list_rnn += err_list
        ADC_err_list_rnn.append(err_list[0])
        GBW_err_list_rnn.append(err_list[1])
        PM_err_list_rnn.append(err_list[2])
        CMRR_err_list_rnn.append(err_list[3])
        PSRR_err_list_rnn.append(err_list[4])

        ADC_pred_list_rnn.append(item1[0])
        GBW_pred_list_rnn.append(item1[1])
        PM_pred_list_rnn.append(item1[2])
        CMRR_pred_list_rnn.append(item1[3])
        PSRR_pred_list_rnn.append(item1[4])

    err_out_list_rnn = init_list_rnn/len(out_list)
    match_out_list_rnn = np.asarray([1., 1., 1., 1., 1.])- err_out_list_rnn
    print match_out_list_rnn
    print np.mean(match_out_list_rnn)

    x_axi = []
    for i in range(len(out_list)):
        x_axi.append(i)
    #print float(num)/len(out_list)

    
    plt.figure(1)
    plt.subplot(121)
    plt_font_size = 17
    plt.title("DNN Relative Error Curve", fontsize = plt_font_size)
    plt.plot(ADC_err_list, "y", label = "ADC", alpha = 0.5)
    plt.plot(GBW_err_list, "b", label = "GBW", alpha = 0.5)
    plt.plot(PM_err_list, "g", label = "PM", alpha = 0.5)
    plt.plot(CMRR_err_list, "r", label = "CMRR", alpha = 0.5)
    plt.plot(PSRR_err_list, "m", label = "PSRR", alpha = 0.5)
    plt.legend(fontsize = plt_font_size, loc = "upper right")
    plt.axis([0, 900, 0, 0.9])
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("Relative Error", fontsize = plt_font_size)
    #plt.show()
    
    plt.subplot(122)
    plt_font_size = 17
    #plt.title("RNN")
    plt.title("RNN Relative Error Curve", fontsize = plt_font_size)
    plt.plot(ADC_err_list_rnn, "y", label = "ADC", alpha = 0.5)
    plt.plot(GBW_err_list_rnn, "b", label = "GBW", alpha = 0.5)
    plt.plot(PM_err_list_rnn, "g", label = "PM", alpha = 0.5)
    plt.plot(CMRR_err_list_rnn, "r", label = "CMRR", alpha = 0.5)
    plt.plot(PSRR_err_list_rnn, "m", label = "PSRR", alpha = 0.5)
    plt.axis([0, 900, 0, 0.9])
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("Relative Error", fontsize = plt_font_size)
    plt.show()
    


    """
    ADC_pred_list = np.asarray(ADC_pred_list)
    ADC_truth_list = np.asarray(ADC_truth_list)
    ADC_sum = 0
    for (item1, item2) in zip(ADC_pred_list, ADC_truth_list):
        ADC_sum += np.fabs(item1 - item2)/item2
    print ADC_sum / len(ADC_pred_list)
    """
   
    
    plt.figure(2)
    plt.subplot(121)
    plt.title("DNN Adc", fontsize = plt_font_size)
    plt.scatter(x_axi, ADC_truth_list, marker = "^", c = "r", s = 50, label = "ground truth")
    #plt.plot(ADC_pred_list, "ko", color = "y", label = "ADC_pred")
    plt.scatter(x_axi, ADC_pred_list, marker = "s", c = "b", s = 15, label = "prediction", alpha = 0.7)
    plt.ylabel("Adc", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    #plt.show()

    plt.subplot(122)
    plt.title("RNN Adc", fontsize = plt_font_size)
    plt.scatter(x_axi, ADC_truth_list, marker = "^", c = "r", s = 50, label = "ground truth")
    #plt.plot(ADC_pred_list, "ko", color = "y", label = "ADC_pred")
    plt.scatter(x_axi, ADC_pred_list_rnn, marker = "s", c = "b", s = 15, label = "prediction", alpha = 0.7)
    plt.ylabel("Adc", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    
    
    
    #plt.plot(GBW_truth_list, "ko", color = "g", label = "GBW_truth")
    #plt.plot(GBW_pred_list, "^", color = "y", label = "GBW_pred", alpha = 0.1)
    plt.figure(3)
    plt.subplot(121)
    plt.title("DNN GBW", fontsize = plt_font_size)
    plt.scatter(x_axi, GBW_truth_list, marker = "^", c = "r", s = 80, label = "ground truth")
    plt.scatter(x_axi, GBW_pred_list, marker = "s", c = "b", s = 10, label = "prediction", alpha = 0.7)
    plt.ylabel("GBW", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    #plt.show()

    plt.subplot(122)
    plt.title("RNN GBW", fontsize = plt_font_size)
    plt.scatter(x_axi, GBW_truth_list, marker = "^", c = "r", s = 80, label = "ground truth")
    plt.scatter(x_axi, GBW_pred_list_rnn, marker = "s", c = "b", s = 10, label = "prediction", alpha = 0.7)
    plt.ylabel("GBW", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    

    
    plt.figure(4)
    plt.subplot(121)
    plt.title("DNN PM", fontsize = plt_font_size)
    plt.scatter(x_axi, PM_pred_list, marker = "^", c = "r", s = 80, label = "prediction")
    plt.scatter(x_axi, PM_truth_list, marker = "s", c = "b", s = 10, label = "ground truth", alpha = 0.7)
    plt.ylabel("PM", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.axis([0, 900, 55, 72])
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    #plt.show()

    plt.subplot(122)
    plt.title("RNN PM", fontsize = plt_font_size)
    plt.scatter(x_axi, PM_pred_list_rnn, marker = "^", c = "r", s = 80, label = "prediction")
    plt.scatter(x_axi, PM_truth_list, marker = "s", c = "b", s = 10, label = "ground truth", alpha = 0.7)
    plt.ylabel("PM", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.axis([0, 900, 55, 72])
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    

    plt.figure(5)
    plt.subplot(121)
    plt.title("DNN CMRR", fontsize = plt_font_size)
    plt.scatter(x_axi, CMRR_pred_list, marker = "^", c = "r", s = 80, label = "prediction")
    plt.scatter(x_axi, CMRR_truth_list, marker = "s", c = "b", s = 10, label = "ground truth", alpha = 0.7)
    plt.ylabel("CMRR", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    #plt.show()

    plt.subplot(122)
    plt.title("RNN CMRR", fontsize = plt_font_size)
    plt.scatter(x_axi, CMRR_pred_list_rnn, marker = "^", c = "r", s = 80, label = "prediction")
    plt.scatter(x_axi, CMRR_truth_list, marker = "s", c = "b", s = 10, label = "ground truth", alpha = 0.7)
    plt.ylabel("CMRR", fontsize = plt_font_size)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    
    
    plt.figure(6)
    plt.subplot(121)
    plt.title("DNN PSRR", fontsize = plt_font_size)
    plt.scatter(x_axi, PSRR_pred_list, marker = "^", c = "r", s= 80, label = "prediction")
    plt.scatter(x_axi, PSRR_truth_list, marker = "s", c = "b", s = 50, label = "ground truth", alpha = 0.7)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("PSRR", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.axis([0, 900, 170, 380])
    #plt.show()

    plt.subplot(122)
    plt.title("RNN PSRR", fontsize = plt_font_size)
    plt.scatter(x_axi, PSRR_pred_list_rnn, marker = "^", c = "r", s= 80, label = "prediction")
    plt.scatter(x_axi, PSRR_truth_list, marker = "s", c = "b", s = 50, label = "ground truth", alpha = 0.7)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("PSRR", fontsize = plt_font_size)
    plt.axis([0, 900, 170, 380])
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    

    x_axi_2 = []
    for i in range(len(real_wl)):
        x_axi_2.append(i)

    plt.figure(7)
    plt.subplot(121)
    #print len(real_wl)
    plt.title("DNN SIZE", fontsize = plt_font_size)
    plt.scatter(x_axi_2, dnn_wl, marker = "^", c = "r", s= 20, label = "prediction")
    plt.scatter(x_axi_2, real_wl, marker = "s", c = "b", s = 1, label = "ground truth", alpha = 0.2)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("M4", fontsize = plt_font_size)
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    #plt.axis([0, 900, 170, 380])
    #plt.show()
    
    plt.subplot(122)
    plt.title("RNN SIZE", fontsize = plt_font_size)
    plt.scatter(x_axi_2, rnn_wl, marker = "^", c = "r", s= 20, label = "prediction")
    plt.scatter(x_axi_2, real_wl, marker = "s", c = "b", s = 1, label = "ground truth", alpha = 0.2)
    plt.xlabel("Test ID", fontsize = plt_font_size)
    plt.ylabel("M4", fontsize = plt_font_size)
    #plt.axis([0, 900, 170, 380])
    plt.legend(fontsize = plt_font_size)
    plt.xticks(fontsize = plt_font_size)
    plt.yticks(fontsize = plt_font_size)
    plt.show()
    



if __name__ == "__main__":
    acc_cal()
