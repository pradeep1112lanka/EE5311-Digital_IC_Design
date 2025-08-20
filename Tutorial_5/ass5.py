import numpy as np
import matplotlib.pyplot as plt

# Given vdd values
vddvec = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8])

# Given frequency vectors
freqvec1 = np.array([3.597717e+08, 5.496954e+08, 7.516428e+08, 9.568004e+08, 1.159311e+09,
                      1.356036e+09, 1.544175e+09, 1.722834e+09, 1.890524e+09])

freqvec2 = np.array([4.410665e+08, 6.774513e+08, 9.318293e+08, 1.192913e+09, 1.453660e+09,
                      1.710315e+09, 1.955991e+09, 2.188518e+09, 2.414532e+09])

# Plot comparison
plt.figure(figsize=(8, 5))
plt.plot(vddvec, freqvec1 / 1e9, marker='o', label='Frequency Set 1')
plt.plot(vddvec, freqvec2 / 1e9, marker='s', label='Frequency Set 2')
plt.xlabel('Vdd (V)')
plt.ylabel('Frequency (GHz)')
plt.title('Comparison of Frequency vs. Vdd')
plt.legend()
plt.grid()
plt.show()

# Print differences
freq_diff = freqvec2 - freqvec1
for i in range(len(vddvec)):
    print(f'Vdd: {vddvec[i]:.1f} V | Freq1: {freqvec1[i]:.2e} Hz | Freq2: {freqvec2[i]:.2e} Hz | Diff: {freq_diff[i]:.2e} Hz')
