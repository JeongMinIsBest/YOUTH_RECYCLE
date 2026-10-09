# 🚮 Data-Driven Solutions to Municipal Waste Issues in Jeonju Using Random Forest 
> 2nd Jeonbuk Youth Big Data Competition – *Woori Bank President’s Award* (Dec 2024)

📊 **Organizers**: Jeonbuk Big Data Technology Exchange Joint Research Association, Woosuk University LINC 3.0 Project Group, Jeonbuk National University Big Data Innovation Convergence College Project Group

👩‍💻 **Planning & Analysis**: Minsu Kang, Gibaek Lee, Hyewon Lee, Jeongmin Lim

🗓 **Project Duration**: October 1, 2024 – October 4, 2024
<br/>
<br/>

## 💬 1. Project Overview 
This project combines public data analysis and machine learning to address improper waste separation and illegal dumping in Jeonju’s studio-apartment areas and residential neighborhoods. It proposes **Recycling Stations** as a policy intervention and focuses the detailed location analysis on **Songcheon 1-dong**.

The original competition proposal identifies the area around **Butnae 5-gil–Butnae 3-gil in Songcheon-dong 2-ga** as the reference location for the intervention.

This repository organizes the project’s datasets, archived notebooks, and reconstructed analysis code. Its purpose is to make the original analysis workflow accessible and reproducible, with the Songcheon neighborhood remaining the focus of the project description.
<br/>
<br/>

## 🗑️ 2. Background and Research Motivation 
The project considers recurring illegal dumping, access to designated waste-separation locations, restrictions on disposal schedules, and the limitations of surveillance and warning signs alone.

The analysis examines:

- Differences in population, housing distribution, and enforcement records across Jeonju’s administrative districts.
- Relationships between these district-level characteristics and estimated waste generation.
- The distribution of housing buildings, illegal-dumping enforcement locations, and commercial activity in Songcheon 1-dong.

These observations support the original Recycling Station proposal and its neighborhood-level spatial review.
<br/>
<br/>

## 🧩 3. Data Composition 
**Primary unit of analysis**: 35 administrative districts (*행정동*) in the supplied Jeonju boundary data. Detailed mapping focuses on Songcheon 1-dong and the Butnae 3-gil–Butnae 5-gil area.

| Dataset | Purpose |
|---|---|
| Jeonju population and household statistics | District-level descriptive analysis and model inputs |
| Housing, residential-building, and officetel records | Building distribution and district-level counts |
| Nationwide municipal waste-generation data | Waste-generation model training |
| Illegal-dumping enforcement records | Enforcement counts and recorded locations |
| Administrative boundaries (GeoJSON) | District mapping and coordinate assignment |
| Restaurant location data | Commercial-activity layer for the Songcheon neighborhood map |
| Previously saved predictions and aggregates | Inputs for reproducing the existing analysis |

Preprocessing includes numeric-field cleaning, district-name standardization, coordinate assignment, missing-value and duplicate checks, dataset integration, and Min–Max scaling.

The clustering variables are **building count, enforcement count, and estimated annual waste generation**. Building and enforcement variables are counts rather than measurements per unit area. The legacy “waste complaints” column is based on enforcement records.

The repository includes supplemental official restaurant coordinates to reconstruct the commercial-activity layer. The default file is dated April 1, 2022; a June 4, 2025 alternative is also retained. These supplemental files should not be assumed to be identical to the restaurant data used in the original competition. Restaurant locations cover one component of commercial activity.

Data sources and processing records are documented in [data_sources.md](docs/data_sources.md) and [commercial_provenance.json](data/processed/commercial_provenance.json).
<br/>
<br/>

## 🔎 4. Methodology 

### 4.1 Machine Learning–Based Prediction
The workflow estimates annual waste generation using **Random Forest** and a comparative **Multi-Layer Perceptron (MLP)** model. Population and household counts serve as inputs to models trained on nationwide municipality-level data, which are then applied to Jeonju’s administrative-district inputs.

The reconstructed training notebook includes regional-group validation and MAE, RMSE, and R² reporting. These checks evaluate municipality-level performance and do not directly measure district-level prediction accuracy.

For the documented reproduction workflow, downstream analysis uses the **previously saved waste-generation predictions**.
<br/>

### 4.2 Exploratory Data Analysis and PCA
- Map district-level population, building counts, enforcement counts, and estimated waste generation.
- Examine correlations before and after excluding population from the clustering features.
- Review PCA explained variance and loadings to understand the normalized feature structure.

The current clustering implementation uses the three normalized features directly. PCA is provided as a diagnostic step.
<br/>

### 4.3 Clustering Analysis
The workflow compares **K-means, PAM-style K-medoids, Gaussian Mixture Models (GMM), and hierarchical clustering** to examine districts with similar characteristics. Silhouette scores, K-means inertia, and medoid-distance diagnostics support review of cluster counts and outliers.
<br/>

### 4.4 Songcheon Neighborhood Mapping
The detailed map overlays **housing buildings, illegal-dumping enforcement locations, and restaurants** in Songcheon 1-dong. The spatial review centers on the original proposal’s **Butnae 5-gil–Butnae 3-gil** area.

The reconstructed map also identifies buildings whose addresses contain these street names. Their extent is a geographic reference for reviewing the proposal, not a surveyed installation boundary or a road centerline.
<br/>
<br/>

## 🌱 5. Original Proposal and Expected Impact 
The original project proposes a Recycling Station intervention in the **Butnae 5-gil–Butnae 3-gil area of Songcheon-dong 2-ga**, within the Songcheon 1-dong analysis target.

Expected benefits include:

- Reduced illegal waste dumping.
- Improved waste separation and recycling participation.
- Greater convenience for residents when disposing of waste.
- Improved neighborhood cleanliness and more informed placement of waste-management facilities.
<br/>
<br/>

## 💻 6. Reproducing the Analysis 
Use Python 3.11 or later. From the repository root, install dependencies and launch Jupyter:

```bash
pip install -r requirements.txt
jupyter notebook
```

Open the notebooks in `notebooks/` and execute cells from top to bottom. Each notebook reads file-based inputs and can run in a separate kernel.

| Order | Notebook | Role in the workflow |
|---|---|---|
| 01 | [Commercial preprocessing](notebooks/01_commercial_preprocessing.ipynb) | Prepare restaurant, housing, and enforcement coordinates |
| 02 | [Model training](notebooks/02_model_training.ipynb) | Review and execute Random Forest and MLP training |
| 03 | [Merge and normalize](notebooks/03_merge_normalize.ipynb) | Integrate existing predictions and counts, then normalize features |
| 04 | [EDA and PCA](notebooks/04_eda_pca.ipynb) | Generate district maps, correlations, and PCA diagnostics |
| 05 | [Clustering](notebooks/05_clustering.ipynb) | Review clustering methods and diagnostics |
| 06 | [Songcheon site analysis](notebooks/06_site_selection.ipynb) | Review the Songcheon neighborhood map and original reference area |

The ZIP includes saved inputs and outputs. A cloned repository may require raw files to be supplied separately; see [data_sources.md](docs/data_sources.md).
<br/>

### Settings for the Songcheon-Focused Workflow
Use the following settings in notebook 03 to retain the saved analysis inputs:

```python
PREDICTION_SOURCE = 'saved'
COUNTS_SOURCE = 'saved'
```

In notebook 06, set:

```python
ANALYZE_AUTO_SELECTED = False
TARGET_DONG = '송천1동'
```

For a review centered on the original proposal, use the **Songcheon detailed-map cell**. The notebook also contains additional candidate-grid calculations; these are supplemental implementation outputs and should not be cited as the original competition’s site-selection findings.

Notebook 01 defaults to `DATASET='historical_2022'`. The standard workflow uses supplied coordinates and requires no geocoding API key. Interactive maps use OpenStreetMap France / HOT and require internet access.
<br/>
<br/>

## 🗂️ 7. Project Structure 
```text
YOUTH_RECYCLE/
├── data/
│   ├── raw/                              # Source files and saved baseline inputs
│   └── processed/                        # Prepared coordinates and provenance
├── notebooks/
│   ├── 01_commercial_preprocessing.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_merge_normalize.ipynb
│   ├── 04_eda_pca.ipynb
│   ├── 05_clustering.ipynb
│   └── 06_site_selection.ipynb
├── results/
│   ├── figures/                          # Charts and static maps
│   ├── maps/                             # Interactive HTML maps
│   └── tables/                           # Predictions, aggregates, summaries, audits
├── src/
│   ├── __init__.py
│   ├── paths.py                          # Shared data and result paths
│   └── geocode.py                        # Optional address-geocoding utility
├── docs/
│   ├── commercial_points_template.csv
│   ├── data_sources.md
│   ├── github_upload.md
│   ├── methodology.md
│   └── validation.json
├── old_versions/                         # Archived notebooks and datasets
│   ├── data/
│   ├── RandomForest_전주연간_쓰레기_배출량_예상_데이터_생성/
│   └── ...                               # Earlier analysis and mapping notebooks
├── README.md
├── README_KR.md
└── requirements.txt
```

The active workflow is in `notebooks/`. Files in `old_versions/` are retained for historical reference and are not required to run the six current notebooks.
<br/>
<br/>