import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 10px;
        width: 100%;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .result-box {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
    }
    .title {
        text-align: center;
        color: #2c3e50;
    }
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open('house_price_model.pkl', 'rb'))

# Header
st.markdown("<h1 class='title'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Get an instant estimate of your house price across top 18 US states</p>", unsafe_allow_html=True)
st.markdown("---")

# Input section
st.markdown("### 📋 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    beds = st.number_input("🛏️ Bedrooms", min_value=1, max_value=10, value=3)
    area_sqft = st.number_input("📐 Area (sq ft)", min_value=500, max_value=10000, value=1500)
    state_code = st.selectbox("📍 State", [
        'CA', 'TX', 'FL', 'NY', 'PA', 'IL', 'OH', 'GA',
        'NC', 'NJ', 'VA', 'WA', 'AZ', 'MA', 'TN', 'MO', 'MD', 'WI'
    ])

with col2:
    baths = st.number_input("🚿 Bathrooms", min_value=1, max_value=10, value=2)
    home_type = st.selectbox("🏡 Home Type", [
        'SINGLE_FAMILY', 'CONDO', 'MANUFACTURED', 'TOWNHOUSE', 'MULTI_FAMILY', 'LOT'
    ])

st.markdown("---")

# Predict button
if st.button("🔍 Predict Price"):
    input_data = pd.DataFrame({
        'beds': [beds],
        'baths': [baths],
        'area_sqft': [area_sqft],
        'state_code': [state_code],
        'home_type': [home_type]
    })

    prediction = model.predict(input_data)
    price = prediction[0]

    st.markdown(f"""
        <div class='result-box'>
            💰 Estimated House Price<br>
            ${price:,.2f}
        </div>
    """, unsafe_allow_html=True)

   
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("🛏️ Bedrooms", beds)
    col2.metric("🚿 Bathrooms", baths)
    col3.metric("📐 Area", f"{area_sqft:,} sqft")


st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>  House Price Prediction App</p>", unsafe_allow_html=True)