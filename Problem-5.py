# Problem-5
import numpy as np
import matplotlib.pyplot as plt
import timeit

# Function to compute DFT using direct computation-------------------
def direct_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    twiddle = np.exp(-2j * np.pi * k * n / N)
    return np.dot(twiddle, x)

# Function to measure the time taken by a given method for DFT computation--------
def measure_time(method, x):
    return timeit.timeit(lambda: method(x), number=10) / 10

# Range of values of n---------------------------------------------
n_values = np.arange(4, 101)
time_direct = []
time_fft = []

# Iterate over different values of n-------------------------------
for n in n_values:
    x = np.random.rand(n)  # Generate n random numbers-------------
    time_direct.append(measure_time(direct_dft, x))
    time_fft.append(measure_time(np.fft.fft, x))

# Plotting the time taken by each method for different values of n
plt.figure(figsize=(10, 6))
plt.plot(n_values, time_direct, label='Direct DFT')
plt.plot(n_values, time_fft, label='FFT')
plt.title('Time taken by DFT methods vs. n')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.grid(True)
plt.show()