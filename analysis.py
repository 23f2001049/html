# analysis.py
# Author: 23f2001049@ds.study.iitm.ac.in

import marimo as mo
import numpy as np

# Cell 1: Define data and create an interactive slider for variable X
# This slider lets users set the X variable; changing it updates downstream cells.
x_slider = mo.ui.slider(
    start=0,
    stop=100,
    step=1,
    value=50,
    label="Select X value",
    show_value=True
)

# Example dependent variable (simulate some relationship)
def compute_y(x):
    # Linear + random noise for demonstration
    rng = np.random.default_rng(seed=1)
    return 2 * x + rng.normal(0, 10)

# Cell 2: Compute Y based on the value of X from the slider
# This cell depends on x_slider and reruns whenever its value changes.
x = x_slider.value
y = compute_y(x)

# Document variable flow: x_slider → x → y

# Cell 3: Dynamic markdown output based on slider value
# Shows mathematical relationship and current variable values interactively.
mo.md(
    f"""
    ## Interactive Data Analysis

    **Selected X:** {x_slider}

    **Computed Y:** {y:.2f}

    $$
    Y = 2X + \\epsilon
    $$
    where $\\epsilon$ is random noise.

    - Move the slider to see Y update dynamically!
    """
)

# Cell 4: Optional plot output (visualizing the relationship)
import matplotlib.pyplot as plt

xs = np.linspace(0, 100, 101)
ys = [compute_y(xv) for xv in xs]
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(xs, ys, label="Y vs X")
ax.axvline(x, color='r', linestyle='--', label=f"X={x}")
ax.axhline(y, color='g', linestyle='--', label=f"Y={y:.2f}")
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Relationship between X and Y")
mo.md(f"### Visualization:\n{mo.as_html(fig)}")

# Each cell above is reactive:
# - Editing the slider (x_slider) triggers updates to x and y, and rerenders markdown and plots.
# - Comments explain the dependence on global variables as required by Marimo.
