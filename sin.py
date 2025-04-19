import numpy as np
import matplotlib.pyplot as plt

# Generate the time axis
duration = 1.0  # Total duration of the signal (in seconds)
sampling_rate = 1000  # Number of samples per second
num_samples = int(duration * sampling_rate)
time = np.linspace(0, duration, num_samples)

# Generate the sinusoidal signal
frequency = 10  # Frequency of the sinusoid (in Hz)
amplitude = 1.0  # Amplitude of the sinusoid
signal = amplitude * np.sin(2 * np.pi * frequency * time)

# Combine time and signal into a single array
data = np.column_stack((time, signal))

# Save the data to a file
path = r'C:\Job\img_proc_tools\data_examples\sin.txt' # Replace with the desired file path
np.savetxt(path, data, delimiter="\t", header="Time\tSignal", comments="")

# Plot the generated signal
plt.plot(time, signal)
plt.title("Generated Sinusoidal Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

print("Data saved successfully.")