# ⚙️ PACE — Precise Adaptation through Continuous Evolution

PACE is a framework for **sim-to-real transfer of diverse robotic systems**, combining data-driven system identification with evolutionary optimization.
It enables accurate actuator modeling and robust adaptation from simulation to reality by explicitly learning physically meaningful dynamics parameters.

---

## What is PACE?

PACE bridges the gap between simulation and real hardware by:

* Estimating actuator and joint dynamics directly from measured data
* Using CMA-ES for robust parameter optimization
* Applying learned parameters to improve sim-to-real locomotion performance
* Supporting multiple robot platforms and actuator types

It is designed to integrate seamlessly with **NVIDIA Isaac Lab** and follows its task and environment conventions.

---

## Installation

### 1. Install Isaac Lab

Follow the official Isaac Lab installation guide:
[https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html)

We recommend using the **conda** or **uv** installation method, as this simplifies running Python scripts from the terminal and managing dependencies.

### 2. Clone this repository

Clone or copy this project separately from the Isaac Lab installation (i.e. outside the `IsaacLab` directory):

```bash
git clone git@github.com:<your-org>/pace-sim2real.git
cd pace-sim2real
```

### 3. Install PACE in editable mode

Using a Python interpreter that has Isaac Lab installed:

```bash
# Use 'PATH_TO_isaaclab.sh|bat -p' instead of 'python'
# if Isaac Lab is not installed in a Python venv or conda environment
python -m pip install -e source/pace_sim2real
```

---

## 📚 Local Documentation Preview (TODO adjust once open sourcing)

Even if the website is not yet public, you can view the documentation locally.

### Quick preview

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

Then open in your browser:

```
http://127.0.0.1:8000
```

---

## 🐾 Running an Example: ANYmal D

### 1. Activate the Isaac Lab environment

```bash
conda activate <isaaclab_env>
cd path/to/pace-sim2real
```

### 2. Collect excitation data

(Alternatively, place your own real-world data in `data/`)

```bash
python scripts/pace/data_collection.py
```

### 3. Run PACE parameter fitting

```bash
python scripts/pace/fit.py
```

This will estimate the actuator and joint parameters using CMA-ES and store results in:

```
logs/pace/<robot_name>/
```

---

## License

© 2025 ETH Zurich, Robotic Systems Lab, Filip Bjelonic

This project is licensed under the Apache License, Version 2.0.
See the LICENSE file for details.

---

## Maintainers

The PACE project is actively maintained by:

- Filip Bjelonic (ETH Zurich, RSL)
- René Zurbrüegg (ETH Zurich, RSL)
- Oliver Fischer (ETH Zurich, RSL)

The maintainers are responsible for reviewing contributions, managing issues, and guiding the technical direction of the framework.

---

## Acknowledgements

We would like to thank the RSL Learning Group for many insightful discussions that influenced the development of PACE. We are especially grateful to Konrad and Matthias for valuable technical input related to electronics and system integration.

We also acknowledge Zichong, Stephan, Efe, Yuntao, René, Clemens, Ryo, Alexander, and Fabio for employing and extending the PACE framework in their own research, providing valuable feedback and practical insights.

We further thank Oliver Fischer and René Zurbrüegg for their direct contributions to the codebase and their ongoing support as project maintainers.

We also thank the early testers — Clemens and Oliver — who evaluated the framework prior to its public release and provided valuable feedback on usability, stability, and documentation improvements.

---

## 🛠 Code Formatting

We provide a pre-commit configuration to automatically format and lint the codebase.

### Install pre-commit

```bash
pip install pre-commit
```

### Enable hooks

```bash
pre-commit install
```

### Run manually

```bash
pre-commit run --all-files
```

---

## 🧩 Troubleshooting

### Pylance: Missing Indexing of Extensions

In some VS Code versions, indexing for Isaac Lab extensions may be incomplete. Add your extension path to `.vscode/settings.json`:

```json
{
  "python.analysis.extraPaths": [
    "<path-to-ext-repo>/source/pace_sim2real"
  ]
}
```

---

### Pylance: Crash / High Memory Usage

If Pylance crashes due to excessive indexing, exclude unused omniverse packages by commenting them out in:

`.vscode/settings.json` → `python.analysis.extraPaths`

Examples of packages that can often be safely excluded:

```json
"<path-to-isaac-sim>/extscache/omni.anim.*",
"<path-to-isaac-sim>/extscache/omni.kit.*",
"<path-to-isaac-sim>/extscache/omni.graph.*",
"<path-to-isaac-sim>/extscache/omni.services.*"
```

---

## Contributing & Feedback

Internal feedback is highly welcome during this phase.
Please report issues, unclear steps, or suggestions directly via GitHub issues or internal channels.

---

## How to cite

If you use **PACE Sim2Real** in your research, please cite our [paper](https://arxiv.org/pdf/2509.06342):

> F. Bjelonic, F. Tischhauser, and M. Hutter,  
> _Towards Bridging the Gap: Systematic Sim-to-Real Transfer for Diverse Legged Robots_, arXiv:2509.06342, 2025.

```bibtex
@article{bjelonic2025towards,
  title         = {Towards Bridging the Gap: Systematic Sim-to-Real Transfer for Diverse Legged Robots},
  author        = {Bjelonic, Filip and Tischhauser, Fabian and Hutter, Marco},
  journal       = {arXiv preprint arXiv:2509.06342},
  year          = {2025},
  eprint        = {2509.06342},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
}
```

---

**PACE** — bringing simulation and reality closer, one parameter at a time.
