import marimo

__generated_with = "0.16.4"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Homework 2
    ==========
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Name:** Vandit Goel  
    **ID:** 1002245699   
    **Email:** vxg5699@mavs.uta.edu   
    **Repo:** git@github.com:vandyG/math-6310.git
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Problem 31

    Generate 100 matrices of size $100\times 100$ whose entries are random Gaussians (i.e., drawn from $\mathcal{N}(0,1)$).  For each matrix, compute its eigenvalues, and after all matrices are generated, plot all of the eigenvalues on one plot (note they will be complex in general).  What do you notice?  Try this experiment for different sizes of matrices; what do you notice?

    Your code must be turned in as an appendix at the end of your homework. In the space below this problem, you should put any figures you generate and your answers to the questions.
    """
    )
    return


@app.cell
def _():
    import numpy as np
    import marimo as mo
    import pandas as pd
    import altair as alt

    return alt, mo, np, pd


@app.cell
def _(mo):
    matrix_size_slider = mo.ui.slider(
        start=20,
        stop=200,
        value=100,
        step=10,
        label="Matrix dimension (n × n)",
        show_value=True,
    )

    distribution_dropdown = mo.ui.dropdown(
        options=[
            "Normal(0,1)",
            "Uniform(0,1)",
            "Uniform(-1,1)",
            "Bernoulli({0,1})",
            "Beta(2,5)",
        ],
        value="Normal(0,1)",
        label="Select Distribution",
    )
    return distribution_dropdown, matrix_size_slider


@app.cell
def _(distribution_dropdown, matrix_size_slider):
    dist = distribution_dropdown.value
    size = matrix_size_slider.value
    return dist, size


@app.cell
def _(dist, np, size):
    if dist == "Normal(0,1)":
        matrices = [np.random.normal(0, 1, (size, size)) for _ in range(100)]
    elif dist == "Uniform(0,1)":
        matrices = [np.random.uniform(0, 1, (size, size)) for _ in range(100)]
    elif dist == "Uniform(-1,1)":
        matrices = [np.random.uniform(-1, 1, (size, size)) for _ in range(100)]
    elif dist == "Bernoulli({0,1})":
        matrices = [np.random.choice([0, 1], (size, size)) for _ in range(100)]
    elif dist == "Beta(2,5)":
        matrices = [np.random.beta(5, 2, (size, size)) for _ in range(100)]
    return (matrices,)


@app.cell
def _(matrices, np):
    eigenvalues = [np.linalg.eigvals(matrix) for matrix in matrices]
    all_eigenvalues = np.concatenate(eigenvalues)
    return (all_eigenvalues,)


@app.cell
def _(
    all_eigenvalues,
    alt,
    dist,
    distribution_dropdown,
    matrix_size_slider,
    mo,
    pd,
):
    alt.data_transformers.enable("vegafusion")

    n = matrix_size_slider.value

    # Prepare a DataFrame with real and imaginary parts
    df = pd.DataFrame(
        {
            "real": all_eigenvalues.real,
            "imag": all_eigenvalues.imag,
        }
    )

    # Create an Altair scatter plot with semi-transparent points
    chart = (
        alt.Chart(df)
        .mark_point(filled=True, opacity=0.45, size=10)
        .encode(
            x=alt.X("real:Q", title="Real Part"),
            y=alt.Y("imag:Q", title="Imaginary Part"),
            tooltip=[
                alt.Tooltip("real:Q", format=".3f"),
                alt.Tooltip("imag:Q", format=".3f"),
            ],
        )
        .properties(
            title=f"Eigenvalues of {dist} Matrices (n = {n})",
            height=400,
            width=400,
        )
        .resolve_scale(x="independent", y="independent")
        .interactive(bind_y=False)
    )

    controls = mo.vstack(
        [
            distribution_dropdown,
            matrix_size_slider,
        ],
        align="start",
        gap="0.75rem",
    )

    layout = mo.vstack([controls, chart], align="center", gap="2rem")
    layout
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Observations
    #### Problem 31

    - Eigenvalues are plotted in the complex plane (real part on x-axis, imaginary part on y-axis).
    - The plotted points form a roughly circular band centered near the origin.
    - The radius increases with the size of the matrices.
        - For n=50, radius ~ 7
        - For n=100, radius ~ 10
        - For n=150, radius ~ 13
        - For n=200, radius ~ 14
    - Point density appears higher near the center and decreases toward the perimeter.
    - Some variability and gaps are visible; the distribution is not perfectly uniform.
    - The plot is less uniform for smaller values of n.

    #### Problem 32
    - The chart for Uniform (0,1) distributions seem to be circular/disk as well. But interestingly has a few outliers around (50,0).
    - The outliers disappear for Uniform (-1, 1) and is predominantly circular/disk.
    - The raidus also seem to increase with the size of the matrix for both Uniform distributions.
    - Similar observations noted for Bernoulli distribution.
    - Beta Distribution seem to always have outliers. But is predominantly circular/disk shaped.
    - The disk shape for these distribution can be attributed to the fact that they can be approximated as a Normal Distribution.
    """
    )
    return


if __name__ == "__main__":
    app.run()
