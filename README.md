Health Study – Statistical Analysis

Project Overview

This project is an individual Data Science assignment that analyzes health data from 800 participants using Python.

The dataset includes age, sex, height, weight, systolic blood pressure, cholesterol, smoking status, and disease status.

The project is divided into two parts. This branch (del1) contains the basic statistical analysis and simulations.

Del 1 – Analysis

The notebook includes:

Data exploration and quality checks

Descriptive statistics and data visualization

Disease occurrence simulation

95% confidence intervals using normal approximation and bootstrap

Hypothesis testing using a one-sided Welch's t-test

Statistical power simulation and effect size comparison

Technologies

Python 3.12.10

Pandas

NumPy

Matplotlib

Seaborn

SciPy

Jupyter Notebook

Project Structure

health-study/
├── data/
│ └── health_study_dataset.csv
├── notebooks/
│ └── health_study_analysis.ipynb
├── .gitignore
├── README.md
└── requirements.txt

How to Run

1. Clone the repository

git clone -b del1 https://github.com/rayya89/health-study.git
cd health-study

2. Create a virtual environment

Use Python 3.12:

py -3.12 -m venv .venv

3. Install the required libraries

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

4. Run the notebook

Open notebooks/health_study_analysis.ipynb in VS Code.

Select the Python kernel from .venv.

Run all cells from top to bottom.

The notebook uses relative file paths to support execution from both the project root and the notebooks directory.

Reproducibility

Fixed random seeds are used for simulations and bootstrap calculations to make the results reproducible.

The notebook was tested successfully using Restart & Run All in VS Code.

References

Documentation and sources supporting the statistical methods are provided in the notebook.
