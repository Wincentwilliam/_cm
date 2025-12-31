# Chaos Theory & Data Engineering: Visualizing the Lorenz Attractor

## 1. Project Overview & Attribution
* **Student Name:** 洪偉升
* **Submission Date:** 2025/12/31
* **Course:** Math and coding
* **Professor:** ccckmit (Chen Zhongcheng)

### Source Declaration (As per Requirement #7)
> **Statement of Originality:** This project utilizes AI (Claude/ChatGPT) for high-level mathematical modeling and Python architecture. I have integrated the components, customized the data engineering pipeline (CSV persistence), and documented the theoretical derivation to demonstrate academic understanding.
> 
> **AI Usage:** Used AI to generate the core Lorenz algorithm and documentation structure.
> **Code Origin:** Modified from AI-generated logic to include data persistence and specialized 3D visualization.

---

## 2. Mathematical Theory: The Lorenz Equations
The **Lorenz Attractor** is a mathematical object that demonstrates **Deterministic Chaos**. It was discovered by meteorologist Edward Lorenz while modeling atmospheric convection.

### The Problem: The Butterfly Effect
In a chaotic system, a tiny change in the initial state (e.g., changing $1.0$ to $1.000001$) leads to a massive difference in the long-term path. This is known as "sensitive dependence on initial conditions."

### The Mathematical Formula
The system is defined by three non-linear ordinary differential equations (ODEs):

$$ \frac{dx}{dt} = \sigma(y - x) $$
$$ \frac{dy}{dt} = x(\rho - z) - y $$
$$ \frac{dz}{dt} = xy - \beta z $$

**Parameter Meanings:**
*   $x, y, z$: Represent the physical state of the fluid (convection rate and temperature gradients).
*   $\sigma$ (Prandtl Number): Ratio of momentum to thermal diffusivity.
*   $\rho$ (Rayleigh Number): Heat transfer ratio (Chaos occurs when $\rho \approx 28$).
*   $\beta$: Represents the geometry of the physical space.

---

## 3. Data Engineering & Tracking Workflow
This project does not just plot numbers; it implements a modern **Data Engineering Pipeline**:

1.  **Numerical Integration:** We use the `scipy.integrate.odeint` library to solve the continuous differential equations. Since computers cannot solve calculus "perfectly," we discretize the time into 5,000 tiny intervals.
2.  **Data Persistence (The CSV Layer):** Instead of keeping results in temporary memory (RAM), we use `pandas` to convert the mathematical results into a structured **CSV (Comma Separated Values)** file. 
    *   **Why?** This allows the chaotic path to be tracked and audited. We can open `chaos_tracking_data.csv` in Excel to inspect the specific $(x, y, z)$ coordinates.
3.  **Graphic Reconstruction:** The final visualization reads the data back from the CSV file rather than the math engine, simulating a real-world scenario where data scientists analyze pre-collected data.

---

## 4. Python Implementation

```python
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# --- STEP 1: MATHEMATICAL LOGIC ---
def lorenz_system(current_state, t, sigma, rho, beta):
    x, y, z = current_state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Constants
SIGMA, RHO, BETA = 10.0, 28.0, 8.0/3.0
initial_condition = [1.0, 1.0, 1.0]
time_steps = np.linspace(0, 50, 5000)

# --- STEP 2: NUMERICAL CALCULATION ---
solutions = odeint(lorenz_system, initial_condition, time_steps, args=(SIGMA, RHO, BETA))

# --- STEP 3: DATA ENGINEERING (CSV EXPORT) ---
df = pd.DataFrame(solutions, columns=['X_Coordinate', 'Y_Coordinate', 'Z_Coordinate'])
df['Timestamp'] = time_steps
csv_file = "chaos_tracking_data.csv"
df.to_csv(csv_file, index=False)

# --- STEP 4: GRAPHICAL RECONSTRUCTION ---
data_to_plot = pd.read_csv(csv_file)
fig = plt.figure(figsize=(12, 9), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
colors = plt.cm.plasma(np.linspace(0, 1, len(data_to_plot)))

for i in range(len(data_to_plot) - 1):
    ax.plot(data_to_plot['X_Coordinate'][i:i+2], 
            data_to_plot['Y_Coordinate'][i:i+2], 
            data_to_plot['Z_Coordinate'][i:i+2], 
            color=colors[i], linewidth=0.8)

ax.set_title("3D Lorenz Attractor: Chaos Theory via Data Engineering", color='white', fontsize=15)
ax.axis('off')
plt.show()

## 5. *Conclusion*
By combining Non-linear Differential Equations with Data Engineering techniques, this project demonstrates how we can capture and visualize the complex geometry of chaos. The resulting "Butterfly" shape is not just a drawing; it is the physical representation of thousands of mathematical calculations tracked, saved to a database (CSV), and reconstructed in 3D space. It proves that even in deterministic systems, complexity and beauty can emerge from simple mathematical rules.