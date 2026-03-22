import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# Load model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Title
st.markdown("<h1 style='text-align: center;'>🚗 Car Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("---")

# Extract categories dynamically (VERY IMPORTANT)
try:
    ohe = model.named_steps['columntransformer'].named_transformers_['onehotencoder']
    car_names = list(ohe.categories_[0])
    companies = list(ohe.categories_[1])
    fuel_types = list(ohe.categories_[2])
except:
    # fallback (if pipeline structure changes)
    car_names = ['Hyundai i20', 'Maruti Swift', 'Honda City']
    companies = ['Hyundai', 'Maruti', 'Honda']
    fuel_types = ['Petrol', 'Diesel', 'LPG']

# Layout
col1, col2 = st.columns(2)

with col1:
    name = st.selectbox("Car Model", car_names)
    year = st.number_input("Year", min_value=1990, max_value=2025, step=1)

with col2:
    company = st.selectbox("Company", companies)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)

fuel_type = st.selectbox("Fuel Type", fuel_types)

st.markdown("---")

# Validation
if kms_driven < 0:
    st.error("Kilometers driven cannot be negative!")

# Predict button
if st.button("🚀 Predict Price"):

    # Create DataFrame
    input_df = pd.DataFrame({
        'name': [name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    try:
        prediction = model.predict(input_df)

        # Output
        st.success(f"💰 Estimated Price: ₹ {prediction[0]:,.2f}")

        # Show input summary
        with st.expander("🔍 See Input Details"):
            st.write(input_df)

    except Exception as e:
        st.error("Something went wrong during prediction!")
        st.write(e)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Machine Learning Project")