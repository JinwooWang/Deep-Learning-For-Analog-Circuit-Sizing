import os
def main():
    os.system("python dataset_generation.py")
    os.system("python running_ngspice.py")
    os.system("python get_data0.py")
    os.system("python change_format.py")
    os.system("python csv_sort.py")

if __name__ == "__main__":
    main()
