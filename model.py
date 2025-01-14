import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import mean_squared_error


def processed_data():
    df = pd.read_csv('used_cars.csv')

    
    df['milage'] = pd.to_numeric(df['milage'].replace({'mi.': '', ',': ''}, regex=True))
   
    df['price'] = pd.to_numeric(df['price'].replace({'\$': '', ',': ''}, regex=True))
  
    df['age'] = 2025 - df['model_year']
    
    df = df[['age', 'milage', 'price']]  
    
    return df

def train_model():
    
    df = processed_data()

    x = df[['age', 'milage']]  
    y = df['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    linear_model = LinearRegression()
    linear_model.fit(x_train, y_train)

    joblib.dump(linear_model, 'car_price_prediction_model.pkl')
    
    y_pred = linear_model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse:.2f}")

    return linear_model, x_test, y_test

def load_model():
    
    return joblib.load('car_price_prediction_model.pkl')


