import streamlit as st
import pandas as pd
import pickle 

st.title("Car Price Prediction")
st.write("This is a simple car price prediction app")

pipe = pickle.load(open('LinearRegressionModel.pkl','rb'))


st.selectbox('Select Company:', ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Ford', 'Mahindra', 'Tata', 'Chevrolet', 'Renault', 'Volkswagen', 'Datsun', 'Nissan', 'Skoda', 'Jeep', 'Audi', 'BMW', 'Mercedes-Benz'], key='company')
# Get trained categories for 'name' column
ohe = pipe.named_steps['columntransformer'].named_transformers_['onehotencoder']
model_options = ohe.categories_[0]   # adjust index depending on your column order

st.selectbox('Select Model:', model_options, key='name')
# st.selectbox('Select Model:', ['Swift', 'i20', 'i10', 'Creta', 'Verna', 'City', 'Amaze', 'Fortuner', 'Innova', 'Ecosport', 'Endeavour', 'XUV500', 'Harrier', 'Altroz', 'Nexon', 'Duster', 'Kwid', 'Polo', 'Vento', 'Rapid', 'Octavia', 'Compass', 'Q3', 'X1', 'X3', 'C-Class'], key='name')
st.selectbox('Year of Purchase', list(range(2000,2026)), key='year')
st.selectbox('Select Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'], key='fuel_type')
st.number_input('Enter Number of Kilometers Travelled:',min_value = 0, step=1000, key='kms_driven')


if st.button('Predict Price'):
    query = pd.DataFrame([[
        st.session_state['name'],
        st.session_state['company'],
        st.session_state['year'],
        st.session_state['kms_driven'],
        st.session_state['fuel_type'],
    ]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    
    st.title("Predicted Price: " +'₹' + str(int(pipe.predict(query)[0])))


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(54, 69, 79, 0.6), rgba(54, 69, 79, 0.6)),
            url("https://5.imimg.com/data5/SELLER/Default/2023/6/313621842/TP/EA/EF/190859789/sports-car-1000x1000.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.title("Car Price Prediction")

# Compare this snippet from Linear%20Regression%20Car%20P01/quikr_car_price_pridictions_prac_01.py: 


