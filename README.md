# subweibull-matrix-freedman


# README

## Overview

This repository contains a Python script for simulating a scalar sub‑Weibull martingale and comparing empirical tail quantiles against various theoretical tail‑bound formulas, including:

* **Our sub‑Weibull bound**: Derived from the new Matrix Freedman–ψₐ inequality.
* **Kroshnin–Suvorikova (KS) bound**: A Bennett‑type result with implicit constants.
* **Tropp’s sub‑Gaussian Freedman bound**: Classical matrix‑Freedman tail bound.

## Files

* `simulate_subweibull.py`: Main simulation script (remove inline comments for clarity).

## Requirements

* Python 3.8+
* Numpy
* SciPy

Install dependencies via:

```bash
pip install numpy scipy
```

## Usage

Run the simulation and display results:

```bash
python simulate_subweibull.py
```

You can adjust parameters at the top of the script:

* `n`: Number of increments
* `alpha`: Sub‑Weibull shape parameter (0 < α ≤ 2)
* `nu`: Scale parameter
* `reps`: Monte Carlo replications
* `d`, `Ctilde`: Constants for Tropp/KS bounds

## Output

The script prints a table of empirical vs.

| δ    | Empirical | Our Bound | KS Bound | Tropp Bound |
| ---- | --------- | --------- | -------- | ----------- |
| 0.10 | ...       | ...       | ...      | ...         |
| 0.05 | ...       | ...       | ...      | ...         |
| 0.01 | ...       | ...       | ...      | ...         |

## License

This project is released under the MIT License.
