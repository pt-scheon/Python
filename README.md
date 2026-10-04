# 🌊 AUV Path Planning & Flare Navigation (`fm3.py` & `fm4.py`)

Autonomous navigation and obstacle avoidance path planning algorithms in Python designed for an **Autonomous Underwater Vehicle (AUV)** navigating through color-coded underwater target flares.

---

## 🎯 Overview

In autonomous underwater robotics missions, an AUV starts at an initial coordinate and must visit multiple target beacons/flares (**Red**, **Green**, **Blue**) while detecting and circumventing stationary obstacles blocking its trajectory.

This branch features two progressive implementations:
* **`fm3.py`**: Baseline path planning featuring full permutation-based Travelling Salesperson Problem (TSP) optimization, collinear obstacle interception checks, orthogonal 4-point detour clearance boxes, and 2D Matplotlib visualization.
* **`fm4.py`**: Confidence-weighted flare navigation. Integrates computer vision/sensor detection confidence scores ($[0.0, 1.0]$) for each flare. Targets with high confidence ($\ge 0.75$) are prioritized along the optimal path, while low-confidence candidates are deferred to the end of the trajectory.

---

## 📐 Mathematical Formulation

### 1. Distance Metric
Given two 2D points $A(x_1, y_1)$ and $B(x_2, y_2)$, distance is calculated via the Euclidean norm:
$$\text{dist}(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### 2. Waypoint Sequence Optimization (TSP)
For $N$ target flares, all permutations $P \in \Pi(\text{flares})$ are evaluated:
$$D(P) = \text{dist}(\text{AUV}, P_1) + \sum_{i=1}^{N-1} \text{dist}(P_i, P_{i+1})$$
The permutation minimizing total distance $D(P)$ is chosen as the traversal order.

### 3. Confidence Filtering (`fm4.py`)
In `fm4.py`, each flare is assigned a confidence metric $c \in [0, 1]$.
* High confidence flares ($c \ge 0.75$) remain in the optimized primary sequence.
* Low confidence flares ($c < 0.75$) are deferred to the tail of the traversal path (`path = [auv] + final + deferred`).

### 4. Collinear Obstacle Interception
An obstacle $O$ lies directly on the segment between waypoints $A$ and $B$ if and only if:
$$\left| \text{dist}(A, O) + \text{dist}(O, B) - \text{dist}(A, B) \right| < 10^{-6}$$
Obstacles on the path are sorted by proximity from $A$ to resolve detours sequentially.

### 5. Orthogonal Box Detour Clearance
For a trajectory segment $\Delta \vec{p} = B - A$ with length $L = \|\Delta \vec{p}\|$:
* **Forward unit vector**: $\vec{u}_{\text{fwd}} = \left(\frac{\Delta x}{L}, \frac{\Delta y}{L}\right)$
* **Perpendicular unit vector**: $\vec{u}_{\perp} = \left(-\frac{\Delta y}{L}, \frac{\Delta x}{L}\right)$

For an obstacle located at $Q$ with safety clearance margin $m$ (default: $0.5$):
* $p_1 = Q - m \cdot \vec{u}_{\text{fwd}}$ (step back before obstacle)
* $p_2 = p_1 + m \cdot \vec{u}_{\perp}$ (sidestep clearance)
* $p_3 = p_2 + 2m \cdot \vec{u}_{\text{fwd}}$ (parallel clearance bypass)
* $p_4 = Q + m \cdot \vec{u}_{\text{fwd}}$ (re-entry to original trajectory)

---

## 🚀 Getting Started

### Prerequisites
Python 3.8+ installed on your system.

### Installation
Clone this repository and checkout the `flare_graph` branch:
```bash
git clone https://github.com/pt-scheon/Python.git
cd Python
git checkout flare_graph
pip install -r requirements.txt
```

### Running the Scripts

#### 1. Baseline Route Optimization (`fm3.py`):
```bash
python3 flare_graph/fm3.py
```

**Sample Input:**
```text
red flare: 10 20
blue flare: 30 40
green flare: 50 10
coords of auv: 0 0
no. of obstacles: 2
coords of 0th obstacle: 5 10
coords of 1th obstacle: 20 30
```

#### 2. Confidence-Weighted Route Optimization (`fm4.py`):
```bash
python3 flare_graph/fm4.py
```

**Sample Input:**
```text
red flare: 10 20
blue flare: 30 40
green flare: 50 10
confidence in Red flare: 0.95
confidence in Blue flare: 0.60
Confidence in Green flare: 0.85
coords of auv: 0 0
no. of obstacles: 1
coords of 0th obstacle: 5 10
```

---

## 📊 Visualization Legend
* ⬛ **Black marker**: Starting position of AUV
* 🔴 **Red marker**: Red target flare
* 🔵 **Blue marker**: Blue target flare
* 🟢 **Green marker**: Green target flare
* 🔘 **Grey marker**: Obstacles
* 🔷 **Cyan line**: Complete plotted trajectory with obstacle bypass detours

---

---

## 🔤 Custom String Methods (`string.py`)

A pure-Python implementation of core string manipulation algorithms built from scratch without standard library string built-ins:
* Case conversion: `upperr()`, `lowerr()`, `capi()`, `tittle()`, `swapc()`
* Search & counting: `counnt()`, `findd()`, `indexx()`
* Boundary checks: `startswithh()`, `endsswith()`
* String transformations: `splitt()`, `joinn()`, `zfilll()`, `centerr()`, `ljustt()`, `rjustt()`
* Character classification: `isalphanumerica()`, `isalphabeta()`, `isascii()`, `isdigitt()`, `isspacee()`, `islowerr()`, `isupperr()`

---

## 📁 Project Structure

```
├── README.md           # Documentation & mathematical explanations
├── string.py           # Custom string algorithms implementation
├── requirements.txt    # Dependencies (numpy, matplotlib)
├── .gitignore          # Git ignore rules for Python artifacts
└── flare_graph/        # Complete flare mapping & navigation algorithm development
    ├── flares.py       # Baseline flare coordinate plotting
    ├── fm.py           # Greedy nearest-flare traversal
    ├── fm2.py          # Permutation-based exhaustive route planner
    ├── fm3.py          # Route optimization with obstacle avoidance
    ├── fm4.py          # Sensor confidence-weighted route optimization
    └── fm5.py          # Multi-flare simulation and comparative benchmarks
```

---

## 🛠 Tech Stack
* **Python 3**
* **NumPy** — Vector manipulation & numerical arrays
* **Matplotlib** — 2D visualization & trajectory rendering
* **Itertools** — Permutation search for path optimization
* **Math** — Geometric hypot and vector calculations
