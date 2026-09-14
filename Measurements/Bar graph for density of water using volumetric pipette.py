#This code produces the bar graph for measurements lab
import numpy as np
import matplotlib.pyplot as plt

# Density measurements (g/mL)
densities = np.array([0.9983, 0.9958, 0.9482, 0.9602, 0.9673])

# Calculate the average and sample standard deviation
average = np.mean(densities)
std_dev = np.std(densities, ddof=1)

# Measurement numbers
measurements = np.arange(1, 6)

# Create the bar graph
plt.figure(figsize=(9, 6))

plt.bar(
    measurements,
    densities,
    yerr=std_dev,
    capsize=5,
    label="Density measurements ± SD"
)

# Average density line
plt.axhline(
    average,
    linestyle="--",
    linewidth=2,
    label=f"Average = {average:.4f} g/mL"
)

# True density line
plt.axhline(
    1.00,
    linestyle="-",
    linewidth=2,
    label="True density = 1.00 g/mL"
)

# Axis titles and graph title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 22.5°C Obtained with the volumetric pipette")

# X-axis labels
plt.xticks(measurements)

# Set y-axis range
plt.ylim(0.90, 1.05)

# Add legend and grid
plt.legend()
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the graph
plt.show()

# Print calculated values
print(f"Average density = {average:.4f} g/mL")
print(f"Sample standard deviation = {std_dev:.4f} g/mL")