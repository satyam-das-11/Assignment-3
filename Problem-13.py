#   Problem-13
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the URL
data_url = "http://theory.tifr.res.in/~kulkarni/noise.txt"
data = np.loadtxt(data_url)

# Number of data points
N = len(data)

# Plot the measurements
plt.figure(figsize=(10, 6))
plt.plot(data, label='Measurements')
plt.title('Measurements')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

# Compute the Discrete Fourier Transform (DFT)
dft = np.fft.fft(data)
plt.figure(figsize=(10, 6))
plt.plot(dft, label='Measurements')
plt.title('DFT of the Measurements')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
# Compute the power spectrum using periodogram
power_spectrum = np.abs(dft) ** 2 / N

# Plot the power spectrum
plt.figure(figsize=(10, 6))
plt.plot(power_spectrum, label='Power Spectrum')
plt.title('Power Spectrum')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.legend()
plt.grid(True)
plt.show()

# Bin the power spectrum in ten k bins
num_bins = 10
bin_size = N // num_bins
binned_power_spectrum = np.zeros(num_bins)

for i in range(num_bins):
    start_idx = i * bin_size
    end_idx = (i + 1) * bin_size
    binned_power_spectrum[i] = np.mean(power_spectrum[start_idx:end_idx])

# Plot the binned power spectrum
plt.figure(figsize=(10, 6))
plt.bar(np.arange(num_bins), binned_power_spectrum, width=0.5)
plt.title('Binned Power Spectrum')
plt.xlabel('Bin')
plt.ylabel('Power')
plt.grid(True)
plt.show()