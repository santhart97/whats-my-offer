# Whats my offer?

## Ironhack Data Analysis Bootcamp Project
![Alt-text](https://www.mynrma.com.au/-/media/my-car/new-vs-old-car.jpg?h=500&w=1140&hash=53254864F72DC160C92B5CD9F6C211F7)


## Topic

For this project, I wanted to implement what I have learned on the Data Analytics Bootcamp by Ironhack to and industry that I am passionate and curious about. So I chose to delve into the automotive industry and to predict the price of a second hand car.
I wanted to see what would the **right** price be for a car I wanted to buy or to sell.

To do this the first step was to find an appropiate dataset I could work with. After much research I found [this](https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes) data set from Kaggle.



## Aim

The aim of the project was to create a model that could predict the *price* of a car given certain variables. 
The purpose of doing this was to find the right offer for the car you are buying or selling.



## Process

1. Exploration and Cleaning 
- I started with 10 different data sets, one for each brand, once I put them together the shape of my dataframe was 101311 rows × 8 columns. Once cleaned the dataframe had 98932 rows × 8 columns.
- I dropped null values and turn the types of columns to floats were necessary.
- The final data looked like this:
![alt](images/clean.png)
![alt](images/dtypes.png)


2. Visualization
-  After the data was cleaned I used matplotlib and seaborn to visualize it in order to have a better idea of what my variables look like.
- I looked for the relation between certain variable and price.
![alt](images/pricexmodel.png)
![alt](images/pricexmileage.png)
![alt](images/pricexengine.png)


3. Modelling
- For the third I looked for the most accurate model.
- I used 5 different models, and found that the most accurate one was **Gradient Boosting Regressor**.


4. Streamlit
- For the last step I used streamlit to create my app.
![alt](images/streamlit.png)



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

Through the use of ML and streamlit I created an app that can predict the price of a car. However, there are many improvements tha could be done in the future.


1. Data:
- In order for the predictions to be more accurate more parameters could be used such as condition of the car, number of doors, type of car (SUV, Convertible, etc...), among many others.


2. Models:
- The model could be optimized or new models can be used in order to fit the data better and have a more accurate prediction.
- Use h2o.


3. Scrapping:
- My initial idea was to scrap data from [Carwow](https://www.carwow.co.uk/used-cars) to see how the offers of their cars compare to my predictions.


4. Deployment:
- I also wanted to use Heroku to deploy my app.


