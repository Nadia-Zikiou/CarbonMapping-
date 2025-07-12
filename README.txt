# CarbonMapping: Remote Sensing Tools for Forest Structure & Carbon Estimation

This repository contains modular code for processing aerial and LiDAR data to support forest structure analysis, vegetation monitoring, and carbon estimation using ArcPy and Python tools.

Developed as part of a Yale Center for Geospatial Solutions (YCGS) project.

---

## 📁 Repository Structure
CarbonMapping/
├── utils/
│ ├── spectral_utils.py # Functions for NDVI, SAVI, NIRv, CIgreen
│ ├── lidar_utils.py # Functions for DSM, DTM, Intensity, Density from LAS
│ └── carbon_utils.py # AGB and Carbon change estimation
├── Spectral_Indices.ipynb # Notebook for computing and saving spectral indices
├── Lidar_Cath.ipynb # LiDAR preprocessing and surface product generation
├── Carbon_Estimation.ipynb # Biomass and carbon tracking between years
├── data/ # (Optional) Example aerial/LiDAR datasets
├── README.md # Project documentation



---

## 🔧 Modules Overview

### 1. **Spectral Indices (utils/spectral_utils.py)**
Calculates:
- **NDVI** (Normalized Difference Vegetation Index)
- **SAVI** (Soil-Adjusted Vegetation Index)
- **NIRv** (Near Infrared Reflectance of Vegetation)
- **CIgreen** (Chlorophyll Index using Green band)

 Source: Aerial imagery from [CT ECO](https://cteco.uconn.edu/data/download/flight2016/index.htm)

---

### 2. **LiDAR Products (utils/lidar_utils.py)**
Converts `.laz` → `.las` and derives:
- **DSM** (Digital Surface Model)
- **DTM** (Digital Terrain Model)
- **Intensity raster**
- **Point density map**

 Source: Lidar data from [CT ECO](https://cteco.uconn.edu/)

---

### 3. **AGB & Carbon Change (utils/carbon_utils.py)**
Estimates:
- Aboveground Biomass (AGB) change
- Carbon stock change and CO₂ equivalent
- Land classification into gain/loss zones
- CSV summary statistics

References:

Brown, S. (1992). Estimating biomass and biomass change of tropical forests: a primer. FAO Forestry Paper 134.

IPCC (2006). 2006 IPCC Guidelines for National Greenhouse Gas Inventories. Volume 4: Agriculture, Forestry and Other Land Use.

Jenkins, J.C., Chojnacky, D.C., Heath, L.S., & Birdsey, R.A. (2003). National-scale biomass estimators for United States tree species. Forest Science, 49(1), 12–35.

Chave, J., Réjou‐Méchain, M., Búrquez, A., et al. (2014). Improved allometric models to estimate the aboveground biomass of tropical trees. Global Change Biology, 20(10), 3177–3190.


---

##  Example Usage

In a Jupyter notebook:

```python
from utils.spectral_utils import calculate_all_indices
from utils.lidar_utils import create_dsm, create_dtm
from utils.carbon_utils import estimate_agb_and_carbon_change



## Requirements

- Python 3.7+
- ArcGIS Pro with ArcPy
- LAS and TIFF aerial data from [CT ECO](https://cteco.uconn.edu/)

# Credits

Developed by [Nadia Zikiou](https://github.com/Nadia-Zikiou) under the Yale Center for Geospatial Solutions (YCGS)
Mentorship: Jenn Marlon

# License

This project is for academic and educational use. Please cite if used in publications.

Contact: zikiounadia@gmail.com