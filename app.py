import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open('best_bike_price_model.pkl', 'rb'))

st.title("🏍️ Bike Price Predictor")

# Define brand and owner lists outside so they're accessible
brand_list = ['Honda', 'Yamaha', 'Bajaj', 'Royal Enfield']
owner_list = ['First', 'Second', 'Third']

# Input fields
year = st.number_input("Model Year", 2000, 2025, step=1)
kms = st.number_input("Kilometers Driven")
power = st.number_input("Power (in HP)")
mileage = st.number_input("Mileage (in kmpl)")
brand = st.selectbox("Brand", brand_list)
owner = st.selectbox("Owner Type", owner_list)

# Predict button
if st.button("Predict Price"):
    try:
        # Derived features
        age = 2025 - year
        brand_encoded = brand_list.index(brand)
        owner_encoded = owner_list.index(owner)

        # Feature order must match training: year, kms, power, mileage, age, brand_encoded, owner_encoded
        input_features = np.array([[year, kms, power, mileage, age, brand_encoded, owner_encoded]])

        # Predict price
        predicted_price = model.predict(input_features)[0]
        st.success(f"💰 Estimated Price: ₹{round(predicted_price)}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
