import streamlit as st
import pandas as pd

import pickle

st.image("https://www.jamjar.com/wp-content/uploads/2018/05/Should-I-sell-my-car_.jpg")

model = pickle.load(open('gbr.pkl','rb'))

def main():
    
    st.title('How much is my car worth?')
    st.markdown("Let's find out.")
    st.write('') 
    st.write('')
    
    my_car = pd.Series()

    car_brands = ['Audi','BMW','Ford','Hyundai','Mercedes','Skoda','Toyota','Vauxhall','Volkswagen']
    brand_selected = st.selectbox("Brand:", car_brands)

    
    for brand in car_brands:
        if brand == brand_selected:
            my_car[f'Brand_{brand}'] = 1
        else:
            my_car[f'Brand_{brand}'] = 0
    
    my_car["Year"] = st.number_input("Year:")

    my_car["Mileage"] = st.number_input("Mileage:")

    my_car["EngineSize"] =  st.number_input("EngineSize:")


    fuel_types = ['Petrol','Diesel', 'Hybrid', 'Electric']
    fuel_selected = st.selectbox("FuelType:", fuel_types)

    for fuel in fuel_types:
        if fuel == fuel_selected:
            my_car[f'FuelType_{fuel}'] = 1
        else:
            my_car[f'FuelType_{fuel}'] = 0



    transmission_types = ['Manual', 'Automatic', 'Semi-Auto']
    transmission_selected = st.selectbox('Transmission:', transmission_types)

    for transmission in transmission_types:
        if transmission == transmission_selected:
            my_car[f'Transmission_{transmission}'] = 1
        else:
            my_car[f'Transmission_{transmission}'] = 0

    st.write(str(my_car))
    
    submit = st.button('Predict')

    if submit:
        ordered_predictors = ['Year', 'EngineSize', 'Mileage', 'Brand_Audi', 'Brand_BMW',
       'Brand_Ford', 'Brand_Hyundai', 'Brand_Mercedes', 'Brand_Skoda',
       'Brand_Toyota', 'Brand_Vauxhall', 'Brand_Volkswagen',
       'Transmission_Automatic', 'Transmission_Manual',
       'Transmission_Semi-Auto', 'FuelType_Diesel', 'FuelType_Electric',
       'FuelType_Hybrid', 'FuelType_Petrol']

        for p in ordered_predictors:
            if p not in my_car.index:
                st.write(f'el predictor {p} no esta en mi car')


        my_car_df = my_car.reindex(index=ordered_predictors).to_frame()
        
        prediction = model.predict(my_car_df.values.T)[0].round(-2)
        st.success(str(prediction))

 

if __name__ == "__main__":
    main()
