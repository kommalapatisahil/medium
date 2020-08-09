#imports
import numpy as np
import matplotlib.pyplot as plt

#1000 points sampled
N = 500
t = np.linspace(0,1,N)
 
s1 = np.sin(50*2*np.pi*t) #pure frequency 50
s2 = np.sin(200*2*np.pi*t) #pure frequency 100
s3 = np.sin(100*2*np.pi*t) #pure frequency 200

s = s1+ 0.6*s2+ 0.2*s3 #mixed with 50, 100 and 200

plt.figure()
plt.plot(t[:100], s[:100]) #200 points for visiblity
plt.xlabel('TIME', c = 'b')
plt.ylabel('AMPLITUDE')
plt.title('MIXED SIGNAL - TIME DOMAIN')

fft = np.fft.fft(s) #magic

freqs = np.linspace(0,1/(t[1]-t[0]), N) #frequency

plt.figure()
plt.plot(freqs[:N//2], np.abs(fft[:N//2])/N, '-r') #/N to normalize peaks
plt.ylabel('AMPLITUDE')
plt.xlabel('FREQUENCY', c = 'r')
plt.title('MIXED SIGNAL - FREQUENCY DOMAIN')
