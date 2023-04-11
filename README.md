<!-- LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ditramadia/Tucil3_13521005_13521019">
    <img src="public/algo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TUGAS KECIL 3</h3>

  <p align="center">
    IF2211 Strategi Algoritma
    <br />
    <a href="doc/Tucil3_13521005-13521019.pdf"><strong>Laporan »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#about-the-project">About The Project</a>
        <ul>
            <li><a href="specification">Specification</a>
            <li><a href="built-with">Built With</a>
        </ul>
    </li>
    <li>
        <a href="#gettingstarted">Getting Started</a>
        <ul>
            <li><a href="#prerequisites">Prerequisites</a>
            <li><a href="#installation">Installation</a>
        </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
    </li>
    <li>
        <a href="#author">Author</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
[![Product Name Screen Shot][product-screenshot]](https://github.com/ditramadia/Tucil3_13521005_13521019)

Tucil 3 of Design of Algorithms (IF2211). Shortest Route Finder, a simple application to solve shortest-path problem using Uniform Cost Search (UCS) and A*. 

### Specification

* Program is able to read a graph represented by adjacency matrix from a text file
* Program is able to find the shortest path using UCS algorithm
* Program is able to find the shortest path using A* algorithm
* Program is able to visualize the solution path and distance
* Bonus: Program is able to visualize the solution path using Google Map API

### Built With

* [![Python][Python.py]][Python-url]
* [![HTML][HTML.html]][HTML-url]

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* gmplot
  ```sh
  pip install gmplot
  ```
* PyQt
  ```sh
  pip install pyqt5
  ```
* matplotlib
  ```sh
  pip install matplotlib
  ```
* networkx
  ```sh
  pip install networkx
  ```
* scipy
  ```sh
  pip install scipy
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/ditramadia/Tucil3_13521005_13521019.git
   ```
2. Go to the repository root folder `Tucil3_13521005_13521019`
   ```sh
   cd Tucil3_13512005_13521019
   ```
3. Run the program `main.py`
   ```sh
   python src/main.py
   ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: public/application-preview.png
[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[HTML.html]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white 
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/HTML