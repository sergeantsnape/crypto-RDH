import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt
from itertools import chain
from collections import Counter, deque

def h_freq(p):
    P = p[:,:,0]
    SimpleList = chain.from_iterable(P)
    return Counter(SimpleList).most_common(1)[0][0]

def genData(data):
        newd = []
        for i in data:
            newd.append(format(ord(i), '08b'))      # generates 8 bit binary data   
        return ''.join(newd)

def hist(img):
    hst=img.histogram()
    l1=hst[0:256]
    for i in range(0, 256):
        plt.bar(i, l1[i],color= '#FF0000',alpha=0.3)
    plt.show()

def dataHiding(fileName,d):
    ogImg = Image.open(fileName)
    hist(ogImg)
    img = ogImg.copy()
    (r,c) = img.size
    Pic = np.asarray(img)
    I = np.transpose(Pic,(1, 0, 2))
    P = I.copy()
    P_k = h_freq(P)
    D = genData(d)

    M = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if P[i][j][0]==255:
                M[i][j] = 1
            else:
                M[i][j] = 0

    for i in range(r):
        for j in range(c):
            if P[i][j][0] > P_k and P[i][j][0] != 255:
                P[i][j][0] += 1
    f=0
    for i in range(r):
        if f:
            break
        for j in range(c):           
            if P[i][j][0] == P_k:
                if len(D)==0:
                    f=1
                    break
                P[i][j][0]+=int(D[0])
                D = D[1:]
            if P[i][j][0] == 255 and M[i][j] == 1:
                D = '1'+D
            if P[i][j][0] == 255 and M[i][j] == 0:
                D = '0'+D

    G = np.transpose(P,(1, 0, 2))
    enc_img = Image.fromarray(G)
    enc_img.save("img\enc.png")
    return P_k

def dataRet(P_k):
    ogImg = Image.open("img\enc.png")
    hist(ogImg)
    img = ogImg.copy()
    (r,c) = img.size
    Pic = np.asarray(img)
    I = np.transpose(Pic,(1, 0, 2))
    P = I.copy()
    # P = p[:,:,0] 
    S = deque()
    k = 1
    decD = ""
    for i in range(r):
        for j in range(c):
            if P[i][j][0] == 255:
                S.append((i,j))
            if P[i][j][0] == P_k and len(S) == 0:
                decD+='0'
                k+=1
            if P[i][j][0] == P_k+1 and len(S) == 0:
                decD+='1'
                k+=1
            if P[i][j][0] == P_k and len(S) != 0:
                (x,y) = S.pop()
                P[x][y][0]-=1
            if P[i][j][0] ==P_k+1 and len(S) != 0:
                (x,y) = S.pop()
            if P[i][j][0] > P_k and P[i][j][0]!=255:
                P[i][j][0]-=1

    G = np.transpose(P,(1, 0, 2)) #P.transpose()
    dec_img = Image.fromarray(G)
    dec_img.save("img\dec.png")
    
    decS = ""

    while True:
        if decD[:8] == "00000000" or not decD:
            break
        decS += chr(int(decD[:8],2))
        decD = decD[8:]

   
    with open("rec_report.txt","w") as f:
        f.write(decS)
    return decS
