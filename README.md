# data-science-student-stress

# Project Overview
This project analyzes student stress factors based on survey data. The analysis includes data preprocessing, exploratory analysis, correlation analysis, and visualization to understand key factors affecting student stress.

# Folder Structure
```
project-root/
│-- data/                   # Contains the dataset
│   ├── Student_Stress_Factors.csv
│-- scripts/                # Contains analysis scripts
│   ├── 01_preprocessing.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_correlation_analysis.py
│   ├── 04_visualization.py
│-- outputs/                # Stores results and generated figures
│-- requirements.txt        # List of dependencies
│-- README.md               # Project documentation
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

## 2. Run Preprocessing Script
Cleans and prepares the dataset.
```bash
python scripts/01_preprocessing.py
```

## 3. Run Exploratory Analysis
Computes summary statistics.
```bash
python scripts/02_exploratory_analysis.py
```

## 4. Run Correlation Analysis
Calculates correlation matrix.
```bash
python scripts/03_correlation_analysis.py
```

## 5. Run Visualization Script
Generates histograms and a correlation heatmap.
```bash
python scripts/04_visualization.py
```

# Requirements
- Python 3.x
- pandas
- seaborn
- matplotlib

# Acknowledgments
- **Dataset Name:** Student Stress Factors  
- **Dataset Author:** Samyak B  
- **Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/samyakb/student-stress-factors)