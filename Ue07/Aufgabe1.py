import matplotlib.pyplot as plt
import os
def Caculate (pic,zahl):    # Durchschnittswert for Farbe,jeweiligen Gesamtwerten for Farbe,
    pixZahl = 0
    farbe1 = 0
    img = plt.imread(pic)   #   read image

    if zahl == 1:
        img[:, :, 0:2] = 0      # Blue
        for j in img:
            for k in j:
                farbe1 += k[2]
                pixZahl += 1

    if zahl==2:
        img[:, :, ::2] = 0      # Green
        for j in img:
            for k in j:
                farbe1 += k[1]
                pixZahl += 1    #像素点计算

    if zahl==3:
        img[:, :, 1:3] = 0  # Red
        for j in img:
            for k in j:
                farbe1 += k[0]
                pixZahl += 1

    farbeDruchschnitt = farbe1 / pixZahl                 # 取得像素平均值
    return  farbeDruchschnitt

def WriteInforamtion (f,farbe):
    datei = open("Farbeidatei.txt", "a")  # 利用参数 ”a“ 创建一个新文本文档
    datei.write('\n')
    datei.write(str(f))     #输出数据
    datei.write(" ")        #空他一个空格
    datei.write(str(farbe)) #输出像素
    datei.write('\n')
    datei.close()
    return

# Main Methode
for f in os.listdir(r'C:\Users\Hong Fang\AppData\Roaming\JetBrains\PyCharm2021.3\scratches\Ue07'):
    a = 0
    if f.endswith('.gif') :
        if f.find("mystery") : # 取得目标六张图片，只有 达芬奇 和 伦勃朗
            while a < 3:       # 取得三原色通道并且输出到文本文档中
                a = a+1

                farbeDruchSchnitt = Caculate(f,a)
                WriteInforamtion(f,farbeDruchSchnitt)
        else:
            continue

# Skript 2
f = open("Farbeidatei.txt")
for i in f:
    print(f.readline().split(' ')[-1])