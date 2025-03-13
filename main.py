import streamlit as st
import pandas as pd
import joblib

model = joblib.load('car_price_prediction_model.pkl')

st.set_page_config(
    page_title="Car Price Prediction Based on Age and Mileage",
    page_icon="🚗",
    layout="centered",
)

st.title("Car Price Prediction Based on Age and Mileage")
st.markdown("""
This app predicts the price of a used car based on its **age** and **mileage**.
The model was trained on historical car data to estimate prices based on these features.
Please enter the car's age (in years) and mileage (in miles) to get the estimated price.
""")

age = st.number_input("Car Age (in years)", min_value=0, max_value=100, value=5)
milage = st.number_input("Mileage (in miles)", min_value=0, max_value=500000, value=50000)

if age < 0 or milage < 0:
    st.warning("Please enter valid positive values for both age and mileage.")

if st.button("Predict Price"):
    if age > 0 and milage > 0:
        input_data = pd.DataFrame({
            'age': [age],
            'milage': [milage]
        })
        
        try:
            predicted_price = model.predict(input_data)
            st.write(f"Estimated Car Price: ${predicted_price[0]:,.2f}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
    else:
        st.error("Please ensure that both car age and mileage are valid (greater than 0).")




