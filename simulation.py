import numpy as np
from scipy.special import gamma, erfinv

d = 4
n = 12
alpha = 1.3
nu = 0.25
Ctilde = 6.0
reps = 10_000
deltas = [0.10, 0.05, 0.01]

Calpha = 2**(2 + 1/alpha) * gamma(1/alpha) / alpha

S_over_sqrtV = np.zeros(reps)

for i in range(reps):
    E = np.random.exponential(size=n)
    mags = nu * E**(1/alpha)
    signs = np.random.choice([-1.0, 1.0], size=n)
    X = signs * mags

    S = X.sum()
    V = np.sum(X**2)
    S_over_sqrtV[i] = S / np.sqrt(V)

V_samples = np.sum((np.random.exponential(size=(reps, n)) * nu)**(2/alpha), axis=1)
v_median = np.median(V_samples)

print(f"Parameters: d={d}, n={n}, α={alpha}, ν={nu}, C̃α={Ctilde}, reps={reps}")
print(f"Median Vₙ  = {v_median:.2f}\n")

header = "   δ    emp/√v   your/√v    KS/√v   Tropp/√v"
print(header)
print("-" * len(header))

for δ in deltas:
    t_emp = np.quantile(S_over_sqrtV, 1-δ)
    t_your = 2*nu * (v_median * np.log(2*n/δ))**(1/alpha)
    t_KS = nu * (Ctilde * v_median * np.log(2*n/δ))**(1/alpha)
    L = 2*nu * v_median**(1/2 - 1/alpha)
    t_tropp = np.sqrt(2*v_median*np.log(d/δ)) + (L/3)*np.log(d/δ)

    print(f"{δ:5.2f}  {t_emp/np.sqrt(v_median):8.2f}  {t_your/np.sqrt(v_median):9.2f}  "
          f"{t_KS/np.sqrt(v_median):8.2f}  {t_tropp/np.sqrt(v_median):10.2f}")
