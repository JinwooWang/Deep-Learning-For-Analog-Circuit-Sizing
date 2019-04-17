import csv
from math import sqrt

def sort_file():
    norm_infile = open("./csv/norm_dataset.csv", "r")
    wl_infile = open("./csv/w_l_dataset_ratio.csv", "r")
    norm_outfile = open("./csv/norm_dataset_sorted_eucsqrt.csv", "w")
    wl_outfile = open("./csv/w_l_dataset_ratio_sorted_eucsqrt.csv", "w")
    euc_outfile = open("./csv/euc_dataset_sorted_eucsqrt.csv", "w")
    csv_write_norm = csv.writer(norm_outfile, dialect = "excel")
    csv_write_wl = csv.writer(wl_outfile, dialect = "excel")
    csv_write_euc = csv.writer(euc_outfile, dialect = "excel")
    norm_list = []
    wl_list = []
    for item in norm_infile:
        item_list = []
        euc = 0
        euc2 = 1.0
        item = item.strip().split(",")
        """
        for ind in item:
            print ind
            euc += float(ind)**2
            euc2 *= float(ind)
            item_list.append(ind)
        """
        euc = (float(item[0])/10.0)**2 + (float(item[1])/1e7)**2 + (float(item[2])/10.0)**2 + (float(item[3])/1e2)**2 + (float(item[4])/1e2)**2
        #euc2 = float(item[0])*float(item[2])*float(item[3])*float(item[4])
        #euc2 = float(item[0])*float(item[1])
        for ind in item:
            item_list.append(ind)
        item_list.append(sqrt(euc))
        #item_list.append(euc2/1e5)
        norm_list.append(item_list)
    for item in wl_infile:
        item_list = []
        item = item.strip().split(",")
        for ind in item:
            item_list.append(ind)
        wl_list.append(item_list)
    L = zip(norm_list, wl_list)
    L.sort(lambda x, y:cmp(x[0][-1], y[0][-1]))

    for (norm, wl) in L:
        csv_write_norm.writerow(norm[:-1])
        csv_write_wl.writerow(wl)
        csv_write_euc.writerow(norm[-1:])
    norm_outfile.close()
    wl_outfile.close()
    euc_outfile.close()

if __name__ == "__main__":
    sort_file()
