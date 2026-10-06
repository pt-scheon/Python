# Python Projects Repository

This repository contains various Python scripts and projects, ranging from autonomous vehicle pathfinding algorithms to custom string manipulation and number conversions.

## 📁 Repository Contents

### 1. 🌊 AUV Flare Navigation (`flare_graph/`)
Path planning and obstacle avoidance algorithms for an Autonomous Underwater Vehicle (AUV).
* **`fm.py`** — Basic greedy nearest-flare traversal.
* **`fm2.py`** — Permutation-based exhaustive route planner (Travelling Salesperson Problem).
* **`fm3.py`** — Route optimization with physical obstacle avoidance and detours.
* **`fm4.py`** — Sensor confidence-weighted route optimization.
* **`fm5.py`** — Multi-flare simulation and comparative benchmarks.
* **`flares.py`** — Baseline 2D coordinate plotting using Matplotlib.

### 2. 🔤 Custom String Methods (`string.py`)
A custom Python script that recreates standard string methods entirely from scratch (e.g., `upper`, `split`, `find`, `isalpha`) without using Python's built-in string functions.

### 3. 🔢 Number to Word Conv  erter (`letter_to_num/`)
Scripts that convert integer numbers into their English word representations based on the Indian Numbering System (Lakh, Crore, Arab).
* **`letter2num.py`** — Interactive script that takes an integer input and prints its word representation.
* **`letter2num2.py`** — Functional version that can automatically convert dictionaries of numbers using dictionary comprehension.

### 4. 📋 List Methods (`auv/list_methods/`)
Demonstrations and implementations of common Python list operations defined from scratch without using in-built list methods, including `insert`, `remove`, `pop`, `reverse`, `sort`, and element deletion.

---

## 🛠 Requirements
To run the visualization scripts in `flare_graph`, install the requirements:
```bash
pip install -r requirements.txt
```
