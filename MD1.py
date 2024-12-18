import numpy as np
import matplotlib.pyplot as plt

# Define arrival rates as percentages from 0% to 100%
arrival_rates_percent = np.arange(0, 101, 1)  # 0% to 100% in steps of 1%
arrival_rates_decimal = arrival_rates_percent / 100  # Convert to decimal for calculation
mu = 1
# Calculate average waiting time (Wq) for each arrival rate as percentage
def data_set_percentage(mu):
    response_times = []
    for lambda_ in arrival_rates_decimal:
        rho = lambda_ / mu
        Wq = (rho**2) / (2 * (1 - rho)) if rho < 1 else float('inf')  # Avoid division by zero
        response_times.append(Wq)
    return response_times


# Get response times for plotting
response_times_percent = data_set_percentage(mu)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(arrival_rates_percent, response_times_percent, label="Average Waiting Time (Wq)", color='teal', marker='o', markersize=3, linewidth=1.5)
plt.fill_between(arrival_rates_percent, response_times_percent, color='teal', alpha=0.2)

# Labeling the axes and the plot
plt.title("Average Waiting Time (Wq) vs. System Utilization (0%-100%)")
plt.xlabel("System Utilization (%)")
plt.ylabel("Average Waiting Time (Wq)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()


# Show the plot
plt.show()
