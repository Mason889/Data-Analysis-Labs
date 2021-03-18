
import matplotlib.pyplot as plt 
import pywt

f_s = 100 # Sampling rate
x=[30, 25, 18, 6, 25, 21, 49, 38, 44, 13, 17, 27, 25, 22, 31, 47, 21, 16, 31, 22, 31, 15, 30, 14, 25, 46, 37, 33, 28, 40, 15, 14, 40, 34, 52, 37, 18, 27, 12, 33, 31, 30, 15, 31, 6, 21, 34, 35, 32, 31, 35, 16, 7, 39, 36, 38, 32, 32, 13, 20, 32, 47, 14, 29, 34, 22, 12, 21, 30, 40, 35, 46, 35, 9, 26, 39, 31, 44, 57, 14, 30, 51, 56, 15, 41, 35, 21, 5, 49, 51, 37, 31, 9, 32, 22, 51, 49, 47, 35, 47, 27, 28, 33, 62, 45, 81, 69, 26, 12, 67, 59, 36, 58, 55, 14, 14, 45, 51, 31, 40, 46, 26, 20, 47, 57, 39, 38, 49, 18, 11, 37, 45, 23, 17, 38, 26, 18, 38, 45, 23, 43, 23, 53, 10, 19, 55, 38, 37, 44, 16, 22]

N=len(x) 
t= range(N)
####### Visualization
fig, (ax1, ax4) = plt.subplots(2,1, sharex = True, figsize = (10,8))
# Signal
ax1.plot(t, x)
ax1.grid(True) 
ax1.set_ylabel("Кількість публікацій") 
ax1.set_title("Динаміка публікацій")
# Wavelet transform, i.e. scaleogram
cwtmatr, freqs = pywt.cwt(x, range(1, N), "mexh", sampling_period = 1 / f_s) 
ax4.pcolormesh(t, freqs, cwtmatr, vmin=-100, cmap = "inferno" ) 
ax4.set_ylim(0,10)
ax4.set_ylabel("Масштаб")
ax4.set_xlabel("Час")
ax4.set_title("Скейлограма на базы вейвлету MexH")
# plt.savefig("./fourplot.pdf") 
plt.show()