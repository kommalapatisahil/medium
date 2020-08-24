#imports 

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib.image as mim
import matplotlib.pyplot as plt
from scipy import spatial
from matplotlib import cm
from PIL import Image


emoji_array = np.load("emojis_16.npy") 
#emoji directory
#reference: https://github.com/sharmaabhishekk/emoji-mosaic-mpl

emoji_mean_array = np.array([ar.mean(axis=(0,1)) for ar in emoji_array]) 
#get mean of each emoji

tree = spatial.KDTree(emoji_mean_array)
#store them in a tree  to search faster 

G_sm = np.array(Image.open('bike.png').resize([20,20]).getdata()).reshape([20,20,3])/256
#open --> resize, smaller --> convert to an array --
#--> reshape to a 3d array --> normalize the pixel values


plt.figure()
plt.imshow(G_sm)
plt.title('Original Image')

indices = []
flattened_img = G_sm.reshape(-1, G_sm.shape[-1]) #flatten the array

#match the pixels with the  closest resembling emoji
#query finds the nearest neighbour index

for pixel in flattened_img:
    pixel_ = np.concatenate((pixel, [1]))
    _, index=tree.query(pixel_)
    indices.append(index)

emoji_matches = emoji_array[indices] 
#from index get the corresponding emoji (flattened)

dim = G_sm.shape[0] 
resized_ar = emoji_matches.reshape((dim, dim, 16, 16,4 ))
#reshape it to form the image. each emoji has the shape (16, 16, 4)
#note: 4 --> R, G, B, alpha

final_img = np.block([[[x] for x in row] for row in resized_ar]) 
#converts individual emoji patches (5 dimensional)
#into a complete image (3 dimensional) using numpy blocks


plt.figure()
plt.imshow(final_img)
plt.title('Emoji mosaic')
plt.savefig('bike_emojied.png')
