# Car Price Prediction Model

## Overview

This project provides a machine learning model that predicts the price of used cars based on their age and mileage. The model is built using a linear regression algorithm and trained on historical car data. The goal is to assist potential buyers and sellers in estimating car prices more accurately.

## Features

- Predicts car prices using age and mileage as input features.
- Trained on a dataset of used cars.
- Provides an interactive web application for users to input data and receive predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit 

## Dataset

The model is trained on a dataset of used cars, which includes the following features:
- **model_year**: The year the car was manufactured.
- **milage**: The distance the car has traveled (in miles).
- **price**: The selling price of the car.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**  
   Open a terminal and run the following command to clone the repository:
   ```bash
   git clone https://github.com/SonuRai598/car-price-prediction.git
   cd car-price-prediction
2. **Set Up a Virtual Environment**
-python -m venv venv
-source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install Required Packages**
Install the necessary Python packages using pip. Make sure you have requirements.txt in your project directory. Run:pip install -r requirements.txt
4. **Prepare the Dataset**
Ensure the dataset file (used_cars.csv) is located in the project directory. This is essential for training the model.
5. **Train the Model**
Before running the web app, you need to train the model. Execute the following command:python train.py
This will generate a car_price_prediction_model.pkl file containing the trained model.
6.**Run the Web Application**
start the Streamlit web application by running:streamlit run app.py

# Making Predictions
-Enter the car's age (in years) and mileage (in miles).
-Click the "Predict Price" button to get the estimated price of the car.

# Model Evaluation
-The model's performance can be assessed using Mean Squared Error (MSE), which is printed during training. Lower values of MSE indicate better performance.

# Contributing
-Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## Social Media
Connect with me:
- [Facebook](https://www.facebook.com/Sonu Chamling) 
- Email: [sonu.anjel007@gmail.com]  



