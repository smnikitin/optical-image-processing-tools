import numpy as np
import matplotlib.pyplot as plt

# Sample input data

path = r'C:\Job\img_proc_tools\data_examples\lin_reg_test.txt'
data = np.loadtxt(path)
x = data[:, 0]
y = data[:, 1]

# Perform linear regression
z, cov = np.polyfit(x, y, 1, cov=True)
error = np.sqrt(np.diag(cov))

# Calculate predicted values
y_pred = z[1] +z[0] * x

# Plot the data points and regression line
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred, color='red', label='Linear Regression')

# Add legend and labels
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

# Add coefficients and statistics
equation = f"y = {z[0]:.2f} * x + {z[1]:.2f}"

slope_std_err = error[0]
intercept_std_err = error[1]
std_err_text = f"y = {z[0]:.2f} * x + {z[1]:.2f}\nSlope Std. Err: {slope_std_err:.2f}\nIntercept Std. Err: {intercept_std_err:.2f}"
plt.text(np.min(x), (np.max(y)-np.min(y))/2, std_err_text, ha='left')

# Display the plot
plt.show()