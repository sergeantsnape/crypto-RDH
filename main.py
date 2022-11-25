from data_hiding import *
from encryption import *

def main():
    import sys
    input = sys.stdin.readline
    fileName = "img\inputMRI.jpg"
    file = open(r"tumor_report.txt", "r")
    data = file.read()
    P_k = dataHiding(fileName,data)
    # print(P_k)
    data_key = str(P_k)
    key = "1234567890qwertyuiopasdfghjklzxcvbnm-=[];,."
    fName = "img\enc.png"
    process_image(fName,key,data_key)
    
    ext_data = dataRet(P_k)
    
    print(ext_data)


if __name__ == '__main__':
    main()