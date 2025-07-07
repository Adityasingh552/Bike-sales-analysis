import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('best_bike_price_model.pkl', 'rb'))

st.title("Bike Price Predictor")

# Input fields
year = st.number_input("Model Year", 2000, 2025)
kms = st.number_input("Kilometers Driven")
power = st.number_input("Power (in HP)")
mileage = st.number_input("Mileage (in kmpl)")
age = 2025 - year

# Example for encoded features (simplified)
brand = st.selectbox("Brand", ['Honda', 'Yamaha', 'Bajaj', 'Royal Enfield'])
owner = st.selectbox("Owner Type", ['First', 'Second', 'Third'])

# Predict
if st.button("Predict Price"):
    try:
        # Compute derived features
        age = 2025 - year
        brand_encoded = brand_list.index(brand)
        owner_encoded = owner_list.index(owner)

        # Create feature array in the correct order
        input_features = np.array([[year, kms, power, mileage, age, brand_encoded, owner_encoded]])

        # Predict
        predicted_price = model.predict(input_features)[0]
        st.success(f"💰 Estimated Price: ₹{round(predicted_price)}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
