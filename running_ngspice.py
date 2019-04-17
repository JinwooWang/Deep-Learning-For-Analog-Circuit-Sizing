import os
folder_list = ["bandwidth", "phase", "CMRR", "PSRR"]

def runing_ng():
    for i in range(4):
        file_list = os.listdir("./src/" + folder_list[i] + "/input/")
        for filename in file_list:
            if filename[-2:] == "sp":
                path = "./src/" + folder_list[i] + "/input/" + filename
                output_path = "./src/" + folder_list[i] + "/output/" + filename[:-3]
                print path
                os.system("ngspice -b -o %s.log %s"%(output_path, path))

if __name__ == "__main__":
    runing_ng()
