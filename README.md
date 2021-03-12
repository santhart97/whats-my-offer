# Whats my offer?

## Ironhack Data Analysis Bootcamp Project
![Alt-text](https://www.mynrma.com.au/-/media/my-car/new-vs-old-car.jpg?h=500&w=1140&hash=53254864F72DC160C92B5CD9F6C211F7)


## Topic

For this project, I wanted to implement the knowledge I gained on the Data Analytics Bootcamp by Ironhack to and industry that I am passionate about. So I chose to delve into the automotive industry and to create a model that predicts the price of a second hand car. I wanted to see what would the right price be for a car I wanted to buy or to sell.

To do this the first step was to find an appropiate dataset I could work with. After much research I found [this](https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes) data set from Kaggle.



## Aim

The aim of the project is to create a model that could predict the appropiate *price* of a car given certain variables; Brand, Year, Mileage, Engine Size, Fuel Type, Transmission. 
The purpose of doing this model is to facilitate the selling or buying by granting the correct cost of a car.



## Process

1. Exploration and Cleaning 
- I started with 10 different data sets, one for each brand, once I put them together the shape of my dataframe was 101311 rows × 8 columns. Once cleaned the dataframe had 98932 rows × 8 columns.
- I dropped null values and turn the types of columns to floats were necessary.
- The final data looked like this:
<p align="center">
  <img src="https://github.com/santhart97/whats-my-offer/blob/main/Images/clean.png">
</p>



2. Visualization
-  After the data was cleaned I used matplotlib and seaborn to visualize it in order to have a better idea of what my variables look like.
- I looked for the relation between certain variable and price.

<p align="center">
  <img src="https://github.com/santhart97/whats-my-offer/blob/main/Images/pricexmodel.png">
</p>

<p align="center">
  <img src="https://github.com/santhart97/whats-my-offer/blob/main/Images/pricexmileage.png">
</p>

<p align="center">
  <img src="https://github.com/santhart97/whats-my-offer/blob/main/Images/pricexengine.png">
</p>

3. Modelling
- For the third I looked for the most accurate model.
- I used 5 different models, and found that the most accurate one was **Gradient Boosting Regressor**.


4. Streamlit
- For the last step I used streamlit to create my app.
<p align="center">
  <img src="https://github.com/santhart97/whats-my-offer/blob/main/Images/streamlit.png">
</p>



### Libraries


1. Exploration and Cleaning
- pandas 


2. Visualization
- seaborn
- matplotlib
- matplotlib.pyplot
- plotly.express 


3. Modelling
- Sklearn
- Matplotlib
- Prettytable 



## Conclusions and Future Work

Through the use of ML and streamlit I created an app that can predict the price of a car based on the variables mentioned above.

There are some improvements that could be done in the future.


1. Data:
- In order for the predictions to be more accurate more parameters could be used such as; condition of the car, number of doors, type of car (SUV, Convertible, etc...), among others.


2. Models:
- The model could be optimized or new models can be used in order to fit the data better and have a more accurate prediction.
- Use h2o.


3. Scrapping:
- My initial idea was to scrap data from [Carwow](https://www.carwow.co.uk/used-cars) to see how the offers of their cars compare to my predictions.


4. Deployment:
- Heroku could be used in the future to deploy the app.


