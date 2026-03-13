# EHD Simulations — Can LLM Agents Care About the World?

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)

## About

This repository contains the simulation code for the arXiv paper proposing **Exocentric Homeostatic Deliberation (EHD)**, a framework for world-directed welfare in persistent LLM agents. EHD extends active-inference-style planning by grounding deliberation in exocentric (other-directed) homeostatic set-points, enabling agents to reason about and maintain the well-being of external systems — not merely their own internal states. Full details and theoretical derivations are available at [neuromorphicinference.com/research/ehd/](https://www.neuromorphicinference.com/research/ehd/).

## Figures

The script produces three figures, each saved as both PDF and PNG in `./figures/`:

1. **`fig_convergence`** — Robbins-Monro convergence of the recalibration rule (Proposition 4)
2. **`fig_ranking_divergence`** — Action-ranking divergence: EHD vs single-step EFE (Proposition 5, mechanism ii)
3. **`fig_welfare_trajectory`** — 24-month EHD welfare simulation (Section 7)

## Usage

```bash
pip install -r requirements.txt
python ehd_simulations.py
```

Figures are saved as PDF and PNG in `./figures/`.

## Citation

```bibtex
@misc{lillo2026ehd,
  author = {Luca Lillo},
  title  = {Can LLM Agents Care About the World?},
  year   = {2026},
  note   = {arXiv preprint}
}
```

## Licence

MIT
