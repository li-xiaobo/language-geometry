[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20709366.svg)](https://doi.org/10.5281/zenodo.20709366)

# Language Geometry: A Unified Geometric Framework for Large Language Models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Core Thesis

**Language is not a sequence of positions, but a sequence of transformations.**

This repository contains code and tools for the paper *"Language Geometry: A Unified Geometric Framework for Understanding Large Language Models"*.

## Key Concepts

- **Difference Vector** `Δ = v_{t+1} - v_t` — The fundamental unit of language
- **Dynamic Subspaces** — Different syntactic relations occupy different low-D subspaces (2-5D)
- **Horizontal Gluing** — `dim(U∪V) = dim(U) + dim(V) - dim(U∩V)`
- **Vertical Coarsening** — Dim reduction → Quantization → Topologization → Logicalization
- **Frame Transformation** — Attention as coordinate change

## Quick Start

### Run on Colab
Click the badge below to open the demo notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/li-xiaobo/language-geometry/blob/main/colab/language_geometry_demo.ipynb)

### Run Locally

```bash
git clone https://github.com/li-xiaobo/language-geometry.git
cd language-geometry
pip install -r requirements.txt

# Run all tests
python tests/run_all_tests.py

# Run individual tools
python tools/tool1_delta_viewer.py
cat > README.md << 'EOF'
# Language Geometry: A Unified Geometric Framework for Large Language Models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Core Thesis

**Language is not a sequence of positions, but a sequence of transformations.**

This repository contains code and tools for the paper *"Language Geometry: A Unified Geometric Framework for Understanding Large Language Models"*.

## Key Concepts

- **Difference Vector** `Δ = v_{t+1} - v_t` — The fundamental unit of language
- **Dynamic Subspaces** — Different syntactic relations occupy different low-D subspaces (2-5D)
- **Horizontal Gluing** — `dim(U∪V) = dim(U) + dim(V) - dim(U∩V)`
- **Vertical Coarsening** — Dim reduction → Quantization → Topologization → Logicalization
- **Frame Transformation** — Attention as coordinate change

## Quick Start

### Run on Colab
Click the badge below to open the demo notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/li-xiaobo/language-geometry/blob/main/colab/language_geometry_demo.ipynb)

### Run Locally

```bash
git clone https://github.com/li-xiaobo/language-geometry.git
cd language-geometry
pip install -r requirements.txt

# Run all tests
python tests/run_all_tests.py

# Run individual tools
python tools/tool1_delta_viewer.py
@software{li_language_geometry_2026,
  author = {Li, Xiaobo},
  title = {Language Geometry: A Unified Geometric Framework for Understanding Large Language Models},
  year = {2026},
  url = {https://github.com/li-xiaobo/language-geometry}
}

### 文件2：LICENSE

```bash
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 Xiaobo Li

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Citation

If you find this work useful, please cite:

```bibtex
@software{Li_Language_Geometry_A_2026,
  author = {Li, Xiaobo},
  title = {Language Geometry: A Unified Geometric Framework for Understanding Large Language Models},
  year = {2026},
  doi = {10.5281/zenodo.20709366},
  url = {https://github.com/li-xiaobo/language-geometry}
}
