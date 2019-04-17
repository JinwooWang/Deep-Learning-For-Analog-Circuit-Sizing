import numpy as np
import matplotlib.pyplot as plt

def acc_cal_RNN():
    infile1 = open("./check/RNN_tst/norm_out_rnn.csv", "r").readlines()
    infile2 = open("./csv_test/norm_dataset.csv", "r").readlines()
    out_list = []
    truth_list = []
    for line in infile1:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        out_list.append(ept_list)
    out_list = np.asarray(out_list)
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
    err_list = init_list/len(out_list)
    cover_list = np.asarray([1., 1., 1., 1., 1.]) - err_list
    print cover_list
    print np.mean(cover_list)
    #print float(num)/len(out_list)

    """
    plt.plot(ADC_err_list, "y", label = "ADC")
    plt.plot(GBW_err_list, "b", label = "GBW")
    plt.plot(PM_err_list, "g", label = "PM")
    plt.plot(CMRR_err_list, "r", label = "CMRR")
    plt.plot(PSRR_err_list, "m", label = "PSRR")
    plt.legend()
    plt.show()
    """

    """
    ADC_pred_list = np.asarray(ADC_pred_list)
    ADC_truth_list = np.asarray(ADC_truth_list)
    ADC_sum = 0
    for (item1, item2) in zip(ADC_pred_list, ADC_truth_list):
        ADC_sum += np.fabs(item1 - item2)/item2
    print ADC_sum / len(ADC_pred_list)
    """

    """
    plt.plot(ADC_pred_list, "y", label = "ADC_pred")
    plt.plot(ADC_truth_list, "b", label = "ADC_truth")
    plt.legend()
    plt.show()
    """

    
    plt.plot(GBW_pred_list, "y", label = "GBW_pred")
    plt.plot(GBW_truth_list, "b", label = "GBW_truth")
    plt.legend()
    plt.show()
    

    """
    plt.plot(PM_pred_list, "y", label = "PM_pred")
    plt.plot(PM_truth_list, "b", label = "PM_truth")
    plt.legend()
    plt.show()
    """

    """
    plt.plot(CMRR_pred_list, "y", label = "CMRR_pred")
    plt.plot(CMRR_truth_list, "b", label = "CMRR_truth")
    plt.legend()
    plt.show()
    """
    
    """
    plt.plot(PSRR_pred_list, "y", label = "PSRR_pred")
    plt.plot(PSRR_truth_list, "b", label = "PSRR_truth")
    plt.legend()
    plt.show()
    """

def acc_cal_DNN():
    infile1 = open("./check/DNN_tst/norm_out_dnn.csv", "r").readlines()
    infile2 = open("./csv_test/norm_dataset.csv", "r").readlines()
    out_list = []
    truth_list = []
    for line in infile1:
        splited_line = line.split(",")
        ept_list = []
        for ind in splited_line:
            ept_list.append(float(ind))
        out_list.append(ept_list)
    out_list = np.asarray(out_list)
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
    err_list = init_list/len(out_list)
    cover_list = np.asarray([1., 1., 1., 1., 1.]) - err_list
    print cover_list
    print np.mean(cover_list)
    #print float(num)/len(out_list)

    """
    plt.plot(ADC_err_list, "y", label = "ADC")
    plt.plot(GBW_err_list, "b", label = "GBW")
    plt.plot(PM_err_list, "g", label = "PM")
    plt.plot(CMRR_err_list, "r", label = "CMRR")
    plt.plot(PSRR_err_list, "m", label = "PSRR")
    plt.legend()
    plt.show()
    """

    """
    ADC_pred_list = np.asarray(ADC_pred_list)
    ADC_truth_list = np.asarray(ADC_truth_list)
    ADC_sum = 0
    for (item1, item2) in zip(ADC_pred_list, ADC_truth_list):
        ADC_sum += np.fabs(item1 - item2)/item2
    print ADC_sum / len(ADC_pred_list)
    """

    """
    plt.plot(ADC_pred_list, "y", label = "ADC_pred")
    plt.plot(ADC_truth_list, "b", label = "ADC_truth")
    plt.legend()
    plt.show()
    """

    
    plt.plot(GBW_pred_list, "y", label = "GBW_pred")
    plt.plot(GBW_truth_list, "b", label = "GBW_truth")
    plt.legend()
    plt.show()
    

    """
    plt.plot(PM_pred_list, "y", label = "PM_pred")
    plt.plot(PM_truth_list, "b", label = "PM_truth")
    plt.legend()
    plt.show()
    """

    """
    plt.plot(CMRR_pred_list, "y", label = "CMRR_pred")
    plt.plot(CMRR_truth_list, "b", label = "CMRR_truth")
    plt.legend()
    plt.show()
    """
    
    """
    plt.plot(PSRR_pred_list, "y", label = "PSRR_pred")
    plt.plot(PSRR_truth_list, "b", label = "PSRR_truth")
    plt.legend()
    plt.show()
    """


if __name__ == "__main__":
    acc_cal_RNN()
