
# Data-Driven Solutions to Municipal Waste Issues in Jeonju Using Random Forest 🚮
> **Award-Winning Project**: 2nd Jeonbuk Youth Big Data Competition – *Woori Bank President’s Award* (Dec 2024)
<br/>
<br/>

## 1. Project Overview
This project addresses persistent issues of improper waste separation and illegal dumping in studio-apartment areas and residential neighborhoods of Jeonju.  
By **combining administrative-district–level public data analysis with machine learning modeling**, the project identifies areas where waste problems occur most frequently and proposes a **data-driven policy intervention through the installation of ‘Recycling Stations,’ including optimal site selection for implementation**.

Rather than stopping at simple prediction or visualization, this project aims to operationalize a full **policy decision-making pipeline**, consisting of:  
**structural cause diagnosis → high-risk area identification → targeted policy intervention**.
<br/>
<br/>

## 2. Background and Research Motivation
Jeonju has repeatedly faced the following issues, particularly in studio-apartment and low-rise residential areas:

- Continuous increase in illegal waste dumping  
- Insufficient designated locations for proper waste separation and frequent non-compliance  
- Resident inconvenience caused by disposal policies limited by specific days and times  
- Limited effectiveness of existing measures such as CCTV installation and warning signage  

These issues are not simply matters of civic awareness, but rather **urban environmental problems shaped by the interaction of population density, housing patterns, and regional structure**.

This project begins with the following research questions:

- Why do waste-related problems repeatedly occur in certain administrative districts?  
- Which structural factors, beyond population size, influence waste generation and concentration?  
- How can data-driven analysis contribute to prioritizing and designing policy interventions?
<br/>
<br/>

## 3. Data Composition
- **Unit of Analysis**: Administrative districts (행정동) in Jeonju
  
- **Data Sources**
  - Population statistics of Jeonju
  - Distribution data of housing, multi-family residences, and officetels
  - Municipal waste generation data
  - Records of illegal dumping enforcement
  - Administrative boundary data (GEOJSON)
  
- **Key Variables**
  - Population size and population density
  - Density of studio-apartment and residential areas
  - Waste generation volume and incident frequency
  
- **Preprocessing**
  - Integration of datasets at the administrative-district level
  - Missing-value handling
  - Feature normalization using Min–Max scaling
<br/>
<br/>

## 4. Methodology

### 4.1 Exploratory Data Analysis (EDA)
- Visualization of population, housing, and waste distributions by administrative district
- Correlation analysis using heatmaps
- Identification of spatial concentration and high-risk areas
<br/>

### 4.2 Machine Learning–Based Prediction
- **Objective**: Estimate annual waste generation for each administrative district in Jeonju
  
- **Models**
  - Random Forest Regressor
  - (Comparative model) Multi-Layer Perceptron (MLP)
  
- **Rationale for Model Selection**
  - Ability to capture nonlinear relationships
  - Robustness to outliers and complex feature interactions
  - Interpretability through feature importance analysis
<br/>

### 4.3 Clustering Analysis
- Application of K-means, K-medoids, Hierarchical Clustering, and Gaussian Mixture Models (GMM)
- Regional typology based on population density, housing density, and waste generation
- Prioritized identification of high-risk clusters
<br/>
<br/>

## 5. Expected Impact
- Reduction in illegal waste dumping in Jeonju
- Decrease in waste-related complaints and improvement of urban aesthetics
- Increased recycling rates and potential reduction in collection costs
- Creation of local employment opportunities and enhanced citizen participation
<br/>
<br/>

## 7. Project Structure
```
YOUTH_RECYCLE-main/
├── data/                                   # Raw and processed datasets
├── RandomForest_Jeonju_Waste_Prediction/
│   ├── Jeonju_Waste_Prediction.ipynb
│   └── result.csv
├── README.md
```
<br/>
<br/>
