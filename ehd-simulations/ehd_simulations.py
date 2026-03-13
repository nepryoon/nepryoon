"""
ehd_simulations.py
==================
Simulation code for:
  "Can LLM Agents Care About the World?
   Exocentric Homeostatic Deliberation (EHD)"

Produces three figures saved as PDF and PNG in ./figures/:
  fig_convergence          — Robbins-Monro convergence of recalibration rule (Prop. 4)
  fig_ranking_divergence   — Action-ranking divergence EHD vs single-step EFE (Prop. 5)
  fig_welfare_trajectory   — 24-month EHD welfare simulation (Section 7)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------
FIGURES_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)


def save_figure(fig: plt.Figure, name: str) -> None:
    """Save *fig* as both PDF and PNG inside FIGURES_DIR."""
    for ext in ("pdf", "png"):
        path = os.path.join(FIGURES_DIR, f"{name}.{ext}")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {path}")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 1 — Robbins-Monro convergence of the recalibration rule (Prop. 4)
# ---------------------------------------------------------------------------
def fig_convergence(rng: np.random.Generator, n_steps: int = 500, n_runs: int = 30) -> None:
    """
    Simulate the stochastic recalibration update
        θ_{t+1} = θ_t - α_t * (θ_t - z_t)
    where α_t = 1/(t+1) (Robbins-Monro schedule) and z_t ~ N(θ*, 1).
    Show mean ± 1 SE over *n_runs* independent runs.
    """
    theta_star = 2.0
    theta_0 = 0.0

    errors = np.zeros((n_runs, n_steps))
    for r in range(n_runs):
        theta = theta_0
        for t in range(n_steps):
            alpha = 1.0 / (t + 1)
            z = rng.normal(theta_star, 1.0)
            theta = theta - alpha * (theta - z)
            errors[r, t] = abs(theta - theta_star)

    mean_err = errors.mean(axis=0)
    se_err = sem(errors, axis=0)

    fig, ax = plt.subplots(figsize=(7, 4))
    steps = np.arange(1, n_steps + 1)
    ax.plot(steps, mean_err, color="steelblue", linewidth=1.8, label="Mean |θ_t − θ*|")
    ax.fill_between(steps, mean_err - se_err, mean_err + se_err,
                    color="steelblue", alpha=0.25, label="±1 SE")
    ax.plot(steps, 1.0 / np.sqrt(steps), color="tomato", linestyle="--",
            linewidth=1.4, label=r"$O(t^{-1/2})$ reference")
    ax.set_xlabel("Step $t$", fontsize=12)
    ax.set_ylabel("Absolute error", fontsize=12)
    ax.set_title("Robbins-Monro Convergence of EHD Recalibration Rule\n(Proposition 4)",
                 fontsize=12)
    ax.legend(fontsize=10)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)
    fig.tight_layout()
    save_figure(fig, "fig_convergence")


# ---------------------------------------------------------------------------
# Figure 2 — Action-ranking divergence: EHD vs single-step EFE (Prop. 5, mech. ii)
# ---------------------------------------------------------------------------
def fig_ranking_divergence(rng: np.random.Generator,
                           n_actions: int = 8,
                           n_horizons: int = 12) -> None:
    """
    Simulate ranking disagreement between EHD (multi-step, exocentric) and
    single-step Expected Free Energy (EFE) across planning horizons.

    EHD scores actions by integrating welfare impact across H steps;
    single-step EFE uses only the immediate next state.
    Divergence is measured as Kendall-τ distance (1 − τ) between the two rankings.
    """
    horizons = np.arange(1, n_horizons + 1)
    divergences = []

    for H in horizons:
        tau_list = []
        for _ in range(200):
            # Random action utility profiles: shape (n_actions, H)
            welfare = rng.standard_normal((n_actions, H))
            # EHD score: cumulative discounted welfare
            discount = np.array([0.95 ** h for h in range(H)])
            ehd_scores = welfare @ discount

            # Single-step EFE score: only first step, plus noise
            efe_scores = welfare[:, 0] + rng.standard_normal(n_actions) * 0.5

            rank_ehd = np.argsort(-ehd_scores)
            rank_efe = np.argsort(-efe_scores)

            # Kendall-τ distance normalised to [0, 1]
            n = n_actions
            discordant = sum(
                1 for i in range(n) for j in range(i + 1, n)
                if (np.where(rank_ehd == i)[0][0] - np.where(rank_ehd == j)[0][0]) *
                   (np.where(rank_efe == i)[0][0] - np.where(rank_efe == j)[0][0]) < 0
            )
            tau_dist = discordant / (n * (n - 1) / 2)
            tau_list.append(tau_dist)

        divergences.append(np.mean(tau_list))

    divergences = np.array(divergences)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(horizons, divergences, color="darkorange", linewidth=2.0,
            marker="o", markersize=5, label="Mean Kendall-τ distance")
    ax.axhline(0.5, color="grey", linestyle="--", linewidth=1.2, label="Random baseline (0.5)")
    ax.set_xlabel("Planning horizon $H$", fontsize=12)
    ax.set_ylabel("Ranking divergence (Kendall-τ distance)", fontsize=12)
    ax.set_title("Action-Ranking Divergence: EHD vs Single-Step EFE\n"
                 "(Proposition 5, mechanism ii)", fontsize=12)
    ax.set_ylim(0, 1)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.5)
    fig.tight_layout()
    save_figure(fig, "fig_ranking_divergence")


# ---------------------------------------------------------------------------
# Figure 3 — 24-month EHD welfare simulation (Section 7)
# ---------------------------------------------------------------------------
def fig_welfare_trajectory(rng: np.random.Generator, months: int = 24) -> None:
    """
    Simulate a 24-month welfare trajectory under EHD vs a passive (no-intervention)
    baseline. The EHD agent applies a corrective action whenever welfare drifts
    outside a homeostatic band around the set-point θ* = 1.0.
    """
    theta_star = 1.0
    band = 0.15
    dt = 1.0  # one month per step
    sigma = 0.12  # environmental noise std

    t = np.arange(months)

    # --- Passive baseline: random walk with slight downward drift ---
    welfare_passive = np.zeros(months)
    welfare_passive[0] = theta_star
    for i in range(1, months):
        welfare_passive[i] = welfare_passive[i - 1] - 0.02 * dt + rng.normal(0, sigma)

    # --- EHD agent: homeostatic control ---
    welfare_ehd = np.zeros(months)
    welfare_ehd[0] = theta_star
    for i in range(1, months):
        prev = welfare_ehd[i - 1]
        noise = rng.normal(0, sigma)
        if prev < theta_star - band:
            correction = 0.10  # upward nudge
        elif prev > theta_star + band:
            correction = -0.10  # downward nudge
        else:
            correction = 0.0
        welfare_ehd[i] = prev + correction - 0.02 * dt + noise

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, welfare_ehd, color="steelblue", linewidth=2.0, label="EHD agent")
    ax.plot(t, welfare_passive, color="tomato", linewidth=1.5,
            linestyle="--", label="Passive baseline")
    ax.axhline(theta_star, color="black", linewidth=0.8, linestyle=":")
    ax.axhline(theta_star + band, color="steelblue", linewidth=0.6,
               linestyle=":", alpha=0.5, label="Homeostatic band")
    ax.axhline(theta_star - band, color="steelblue", linewidth=0.6,
               linestyle=":", alpha=0.5)
    ax.fill_between(t, theta_star - band, theta_star + band,
                    color="steelblue", alpha=0.07)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("World welfare $W_t$", fontsize=12)
    ax.set_title("24-Month EHD Welfare Simulation (Section 7)", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.5)
    fig.tight_layout()
    save_figure(fig, "fig_welfare_trajectory")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)

    print("Generating fig_convergence …")
    fig_convergence(rng)

    print("Generating fig_ranking_divergence …")
    fig_ranking_divergence(rng)

    print("Generating fig_welfare_trajectory …")
    fig_welfare_trajectory(rng)

    print("\nDone. All figures saved to ./figures/")
