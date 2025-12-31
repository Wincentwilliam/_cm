import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. MATHEMATICAL MODELING (The Lorenz System)
def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Parameters for the "Butterfly Attractor"
params = {"sigma": 10.0, "rho": 28.0, "beta": 8.0/3.0}
initial_condition = [1.0, 1.0, 1.0]
t = np.linspace(0, 50, 5000) # 50 seconds, 5000 data points

# 2. COMPUTATION
print("Computing chaotic trajectory...")
solution = odeint(lorenz_system, initial_condition, t, 
                  args=(params["sigma"], params["rho"], params["beta"]))

# 3. CSV EXPORT (Data Persistence)
# We store the math results into a structured table (DataFrame)
df = pd.DataFrame(solution, columns=['X', 'Y', 'Z'])
df['Time'] = t
csv_filename = "lorenz_data.csv"
df.to_csv(csv_filename, index=False)
print(f"Mathematical data successfully saved to: {csv_filename}")

# 4. VISUALIZATION (Generating the Graphic from the CSV)
# We read the data back from the CSV to prove data integrity
data = pd.read_csv(csv_filename)

fig = plt.figure(figsize=(12, 9), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Create a beautiful gradient color based on time steps
colors = plt.cm.magma(np.linspace(0, 1, len(data)))

# Plotting the path
for i in range(len(data) - 1):
    ax.plot(data['X'][i:i+2], data['Y'][i:i+2], data['Z'][i:i+2], 
            color=colors[i], linewidth=0.8, alpha=0.7)

# Formatting the graphic
ax.set_title("3D Lorenz Attractor: Chaos in Data", color='white', fontsize=16)
ax.axis('off') # Hide axes for a clean artistic look

print("Displaying graphic...")
plt.show()