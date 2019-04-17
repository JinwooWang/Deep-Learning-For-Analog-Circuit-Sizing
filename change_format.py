import csv

def change_format(filename):
    infile = open("./csv/" + filename, "r").readlines()
    outfile = open("./csv/%s_ratio.csv"%(filename[:-4]), "w")
    csv_write = csv.writer(outfile, dialect = "excel")
    for item in infile:
        item = item.strip().split(",")
        temp_list = []
        for ind in item:
            temp_list.append(float(ind))
        ratio_list = []
        print temp_list
        for i in range(len(temp_list)/2):
            tmp = temp_list[2*i]/temp_list[2*i + 1]
            ratio_list.append(str(tmp))
        csv_write.writerow(ratio_list)
    outfile.close()

if __name__ == "__main__":
    change_format("w_l_dataset.csv")
