import os
def IDE():
    os.system("mkdir src")
    os.system("mkdir ./src/bandwidth")
    os.system("mkdir ./src/phase")
    os.system("mkdir ./src/CMRR")
    os.system("mkdir ./src/PSRR")
    
    os.system("mkdir ./src/bandwidth/input")
    os.system("mkdir ./src/bandwidth/output")
    os.system("mkdir ./src/bandwidth/ADC_GBW")
    
    os.system("mkdir ./src/phase/input")
    os.system("mkdir ./src/phase/output")
    os.system("mkdir ./src/phase/PM")
    
    os.system("mkdir ./src/CMRR/input")
    os.system("mkdir ./src/CMRR/output")
    os.system("mkdir ./src/CMRR/cmrr")
    
    os.system("mkdir ./src/PSRR/input")
    os.system("mkdir ./src/PSRR/output")
    os.system("mkdir ./src/PSRR/psrr")
    

if __name__ == "__main__":
    IDE()
