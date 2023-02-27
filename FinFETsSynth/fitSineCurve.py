import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function to fit (sine function)
def sine_func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# Define the given points
xdata = np.array([0, 1, 2, 3])
ydata = np.array([1, 0, -1, 0])

# Fit the function to the data using curve_fit
popt, pcov = curve_fit(sine_func, xdata, ydata)

# Print the optimized parameters
print(popt)

# Generate some x values to plot the curve
xplot = np.linspace(0, 2, 100)

# Plot the data and the fitted curve
plt.plot(xdata, ydata, 'o', label='data')
plt.plot(xplot, sine_func(xplot, *popt), '-', label='fit')
plt.legend()
plt.show()