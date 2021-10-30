#import numpy
import numpy as np
#import matplotlib
from matplotlib import pyplot as plt

x0,y0 = input('masukkan kordinat 1: ').split()
x1,y1 = input('masukkan kordinat 2: ').split()

#konversi input sebelum (str -> int)
x0=int(x0)
x1=int(x1)
y0=int(y0)
y1=int(y1)

#array titik kordinat
data = np.array([[0,0],[0,0]])

#selisih X
deltX = x1 - x0
#selisih Y
deltY = y1 - y0

#penentuan step
if abs(deltY)>abs(deltX):
    step = abs(deltY)
else:
    step = abs(deltX)

z=1
#kordinat 1
data = np.append(data, [[x0,y0]], axis=0)
data = np.delete(data, 0, 0)
data = np.delete(data, 0, 0)
xcord = x0
ycord = y0
while x0!=x1 and y0!=y1:
    z+=1
    if deltX < 0 and deltY < 0:
        deltX=abs(deltX)
        deltY=abs(deltY)
    xINC = deltX/step
    yINC = deltY/step
    xcord = xcord + xINC
    ycord = ycord + yINC
    x0 = round(xcord)
    y0 = round(ycord)
    print(x0, ",", y0)
    data = np.append(data, [[x0,y0]], axis=0)
    if z >= 10:
        print('Kordinat Tidak Dapat Diselesaikan')
        exit()
        break

#menampilkan hasil titik dalam array
x, y = data.T
plt.scatter(x,y)
plt.show()
