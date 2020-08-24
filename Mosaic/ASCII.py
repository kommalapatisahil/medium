import string
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
%matplotlib inline

siz = 200
im = Image.open("bike.png").resize([siz, siz])
#open and resize

im2 = im.convert(mode = 'L')
#convert to greyscale

im4 = np.array(im2.getdata()).reshape([siz, siz])
#convert image to array (flattened) --> reshape 
print('Image loaded.')

asci =  r"QG@#$%?*+^)/;:!,'.` " #asci2 = r"B8&WM#YXQO{}[]()I1i!pao;:,.    "
#ASCII directory
#check out the alternate verion using asci2!

im7 = []
for i in range(siz):
    imtemp = ""
    for j in range(siz):
        imtemp+= asci[(len(asci)-1)*im4[i,j]//256]
    im7.append(imtemp)
#get the proportion of 256 and replace with an ASCII charecter.    
print('Image Converted.')
    
with open('bike_ascii.txt', 'w') as text:
    for i in im7:
        text.write(i)
        text.write('\n')
print('Image written to .txt file.')
