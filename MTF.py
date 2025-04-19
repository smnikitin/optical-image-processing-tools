# Example usage:
# Assuming you have a grayscale image stored in a numpy array called 'image'
# and you want to plot a cross-sections

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# Read your image here and store it in the 'image' variable
# Specify the path to the image file on your C drive
image_path = r'C:\Job\img_proc_tools\data_examples\mtf.png'

# Open the image using openCV and Convert to grayscale

image= cv.imread(image_path)

# Select ROI
r = cv.selectROI("select the area", image)

# Convert to the grayscale image 
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
# Crop image array
image_array = image_gray[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Create global variables for the initial coordinates and cross-section lines
initial_y = image_array.shape[0] // 2 
cross_section_horizontal = image_array[initial_y, :]

# Calculate the first derivative
derivative_cross_section_horizontal  = np.gradient(cross_section_horizontal )

# Calculate the absolute value of the derivative
abs_derivative_cross_section_horizontal = np.abs(derivative_cross_section_horizontal)

# Perform 1D FFT for MTF
signal = np.fft.fft(abs_derivative_cross_section_horizontal )
MTF = np.abs(signal)
n = len(abs_derivative_cross_section_horizontal)  # Length of the signal
dt = 1  # Time step (assuming evenly spaced time points)
freq = np.fft.fftfreq(n, dt) # Calculate the frequency axis for plotting

#Calulate MTF50
min_val = np.min(MTF)
max_val = np.max(MTF)
middle_value = (max_val - min_val) / 2
index = np.abs(MTF - middle_value).argmin()
MTF50 = freq[index]
print ("mtf50:", MTF50 )

# Create a figure and axes with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(9, 9))

# Plot the original image on the left subplot
ax1.imshow(image_array , cmap='gray')
ax1.axhline(initial_y, color='red', linestyle='--')
ax1.set_title('Original Image with Cross-Section Lines')

# Plot the initial horizontal cross-section on the top-right subplot
ax2.plot(cross_section_horizontal)
ax2.set_xlabel('Distance along the edge in Pixels')
ax2.set_ylabel('Intensity')
ax2.set_title('Edge Spread Function')

# Plot the initial vertical cross-section on the bottom-left subplot

ax3.plot(abs_derivative_cross_section_horizontal )
ax3.set_xlabel('Distance along the edge in Pixels')
ax3.set_ylabel('Intensity')
ax3.set_title('Line Spread Function')

# Plot the initial vertical cross-section on the bottom-left subplot

ax4.plot(freq, MTF)
ax4.plot(MTF50, middle_value , 'ro')
ax4.axhline(y=middle_value, color='r', linestyle='--')
ax4.axvline(x=MTF50, color='r', linestyle='--')
ax4.set_xlabel('Line Pairs per Pixel')
ax4.set_ylabel('Intensity')
ax4.set_title('Modulation Transfer Function')
ax4.set_xlim(0, 0.5)

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

# http://www.mathworks.com/matlabcentral/fileexchange/28631-slant-edge-script/
# https://github.com/bvnayak/PDS_Compute_MTF/blob/master/README.rst
# http://www.quickmtf.com/slantededge.html