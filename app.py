import streamlit as st

st.title("🏡 House Price Prediction App")
st.write("Enter details below to predict house prices.")

size = st.number_input("🏠 House Size (sq ft)")
bedrooms = st.number_input("🛏 Number of Bedrooms")
location_score = st.slider("📍 Location Score", 1, 10)

if st.button("Predict Price"):
    import pickle
    import pandas as pd

    # Load the model
    with open("/Users/venkey/Desktop/ML/House_price_prediction/house_price_model.pkl", "rb") as file:
        model = pickle.load(file)

    # Create DataFrame for user input
    user_input = pd.DataFrame([[size, bedrooms, location_score]], 
                              columns=['Size (sq ft)', 'Bedrooms', 'Location_Score'])

    # Predict
    predicted_price = model.predict(user_input)[0]
    st.success(f"🏡 Estimated House Price: ${predicted_price:,.2f}")