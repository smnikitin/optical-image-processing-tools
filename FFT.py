import numpy as np
import matplotlib.pyplot as plt

# Open and read the file
# Replace with the actual file path

path = r'C:\Job\img_proc_tools\data_examples\sin.txt'
data = np.loadtxt(path, skiprows=1)

# Separate time and signal columns
time = data[:, 0]
signal = data[:, 1]

# Perform 1D FFT
fft_result = np.fft.fft(signal)


# Calculate the frequency axis for plotting
n = len(signal)  # Length of the signal
dt = time[1] - time[0]  # Time step (assuming evenly spaced time points)
freq = np.fft.fftfreq(n, dt)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot the original data
ax1.plot(time, signal)
ax1.set_title("Original Data")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")

# Plot the FFT results
ax2.plot(freq, np.abs(fft_result))
ax2.set_title("FFT Result")
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.set_xlim(0, 100)  # Set the X-axis limits to range from 0 to 100


# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()