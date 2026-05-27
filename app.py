import streamlit as st
import numpy as np
import joblib

model = joblib.load('models/car_price_model.pkl')

st.title("🚗 Car Price Predictor")
st.markdown("Predict the price of a car using **Random Forest Regressor**.")

col1, col2 = st.columns(2)

with col1:
    wheelbase    = st.number_input("Wheelbase",        80.0,  120.0, 98.0,  step=0.1)
    carlength    = st.number_input("Car Length",      140.0,  210.0, 170.0, step=0.1)
    carwidth     = st.number_input("Car Width",        60.0,   80.0,  65.0, step=0.1)
    carheight    = st.number_input("Car Height",       45.0,   60.0,  54.0, step=0.1)
    curbweight   = st.number_input("Curb Weight",    1500,    4100,  2500)
    enginesize   = st.number_input("Engine Size",      60,     330,   130)
    boreratio    = st.number_input("Bore Ratio",        2.5,    4.0,   3.2, step=0.1)

with col2:
    stroke       = st.number_input("Stroke",            2.0,    4.5,   3.2, step=0.1)
    compratio    = st.number_input("Compression Ratio",  7.0,   23.0,   9.0, step=0.1)
    horsepower   = st.number_input("Horsepower",        45,     290,   100)
    peakrpm      = st.number_input("Peak RPM",        4150,    6600,  5200)
    citympg      = st.number_input("City MPG",          13,      49,    25)
    highwaympg   = st.number_input("Highway MPG",       16,      54,    30)
    symboling    = st.selectbox("Symboling (Risk)", [-2, -1, 0, 1, 2, 3])

# Categorical encoded as numbers (use median values as defaults)
fueltype     = st.selectbox("Fuel Type",     [0, 1], format_func=lambda x: "Diesel" if x==0 else "Gas")
aspiration   = st.selectbox("Aspiration",    [0, 1], format_func=lambda x: "Std" if x==0 else "Turbo")
doornumber   = st.selectbox("Door Number",   [0, 1], format_func=lambda x: "Four" if x==0 else "Two")
carbody      = st.selectbox("Car Body",      [0, 1, 2, 3, 4],
                             format_func=lambda x: ["Convertible","Hardtop","Hatchback","Sedan","Wagon"][x])
drivewheel   = st.selectbox("Drive Wheel",   [0, 1, 2], format_func=lambda x: ["4WD","FWD","RWD"][x])
engineloc    = st.selectbox("Engine Location",[0, 1], format_func=lambda x: "Front" if x==0 else "Rear")
enginetype   = st.selectbox("Engine Type",   [0, 1, 2, 3, 4, 5, 6])
cylinders    = st.selectbox("Cylinders",     [0, 1, 2, 3, 4, 5, 6])
fuelsystem   = st.selectbox("Fuel System",   [0, 1, 2, 3, 4, 5, 6, 7])
brand        = st.selectbox("Brand",         list(range(0, 22)))

if st.button("Predict Price", use_container_width=True):
    input_data = np.array([[symboling, fueltype, aspiration, doornumber,
                            carbody, drivewheel, engineloc, wheelbase,
                            carlength, carwidth, carheight, curbweight,
                            enginetype, cylinders, enginesize, fuelsystem,
                            boreratio, stroke, compratio, horsepower,
                            peakrpm, citympg, highwaympg, brand]])

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Car Price: **${prediction:,.2f}**")