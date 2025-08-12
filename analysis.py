# email: 23f2001049@ds.study.iitm.ac.in

import marimo

__generated_with = "0.4.15"
app = marimo.App()


# Cell 1: Importing libraries and loading data
# This cell initializes the dataset
@app.cell
def __load_data():
    import numpy as np
    import pandas as pd

    # Generate a synthetic dataset
    np.random.seed(0)
    df = pd.DataFrame({
        "x": np.linspace(0, 100, 200),
    })
    df["y"] = 2.5 * df["x"] + np.random.normal(0, 25, size=len(df))
    df.head()
    return df, np, pd


# Cell 2: Create an interactive slider
# This slider controls the slope used in a comparison line
@app.cell
def __slider():
    import marimo as mo

    slope_slider = mo.ui.slider(1.0, 5.0, step=0.1, value=2.5, label="Slope for comparison line")
    slope_slider
    return slope_slider


# Cell 3: Plot the data and dynamic comparison line
# Depends on the slider from previous cell and the dataset
@app.cell
def __plot(slope_slider, df, np):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["x"], df["y"], label="Data", alpha=0.7)

    slope = slope_slider.value
    comparison_line = slope * df["x"]
    ax.plot(df["x"], comparison_line, color="red", label=f"y = {slope:.2f}x")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Scatter Plot with Adjustable Comparison Line")
    ax.legend()
    fig.tight_layout()
    fig
    return fig


# Cell 4: Dynamic markdown output
# Generates text based on the current slope
@app.cell
def __dynamic_text(slope_slider):
    import marimo as mo

    slope = slope_slider.value
    description = f"""
    ### Analysis Output

    You selected a slope of **{slope:.2f}** for the comparison line.

    This helps analyze the relationship between `x` and `y` in the dataset.
    """
    mo.md(description)
    return description


# Cell 5: Add markdown explaining the data flow between cells
@app.cell
def __comments():
    import marimo as mo

    mo.md("""
    ### Data Flow Explanation

    - The dataset is generated in **Cell 1**.
    - The interactive **slider widget** in **Cell 2** lets users choose a slope.
    - **Cell 3** uses both the dataset and slider value to draw a dynamic line.
    - **Cell 4** provides a **markdown explanation** that updates with the slider.
    """)
