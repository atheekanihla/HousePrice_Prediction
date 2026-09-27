# House Price Prediction

## Project Overview

This project uses Machine Learning to predict house values based on different property and location features.

The project uses the California Housing dataset and demonstrates a complete Machine Learning workflow, including data exploration, preprocessing, model training, evaluation, model comparison, feature importance analysis, and prediction of new house values.

## Objectives

* Explore and understand the housing dataset.
* Check and prepare the data for Machine Learning.
* Perform exploratory data analysis (EDA).
* Identify relationships between housing features and house values.
* Train regression models.
* Evaluate and compare model performance.
* Identify important features used by the model.
* Make predictions for new house data.
* Save the trained Machine Learning model for future use.

## Dataset

The project uses the California Housing dataset provided through Scikit-learn.

The dataset contains:

* 20,640 observations
* 8 input features
* 1 target variable

### Features

* `MedInc` – Median income
* `HouseAge` – Median house age
* `AveRooms` – Average number of rooms
* `AveBedrms` – Average number of bedrooms
* `Population` – Population
* `AveOccup` – Average house occupancy
* `Latitude` – Geographic latitude
* `Longitude` – Geographic longitude

### Target

* `MedHouseVal` – Median house value

## Machine Learning Models

Two regression models were implemented:

1. Linear Regression
2. Random Forest Regression

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

The models were then compared based on their evaluation results.

## Exploratory Data Analysis

The project includes:

* Dataset inspection
* Missing-value analysis
* Statistical analysis
* House-value distribution visualization
* Median income vs house-value analysis
* Correlation heatmap
* Feature-importance analysis

## Project Structure

```text
HousePrice_Prediction/
│
├── data/
│   └── housing.csv
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── src/
│   ├── download_data.py
│   ├── house_price_model.pkl
│   └── predict.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook
* VS Code

## How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the prediction script

```bash
python src/predict.py
```

## Model Prediction

The trained Random Forest model is saved as:

```text
src/house_price_model.pkl
```

The `predict.py` script loads the saved model and uses housing features to generate a predicted house value.

## Future Improvements

* Perform hyperparameter tuning.
* Improve feature engineering.
* Experiment with additional regression algorithms.
* Create a user-friendly web interface for predictions.
* Deploy the prediction model as a web application.
* Add interactive visualizations.

## Disclaimer

This project is an educational Machine Learning project. The predicted values are model estimates based on the California Housing dataset and should not be treated as professional real-estate valuations.
