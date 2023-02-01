import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from scipy.stats import skew
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_validate, cross_val_score
from sklearn import metrics


st.set_page_config("House Price Prediction App",
                   page_icon="https://thumbs.dreamstime.com/b/flat-house-icon-vector-69856517.jpg")  # page title

img = Image.open(
    "/Users/anilfurkanembel/Desktop/Studies/Immo_Analyses_Visualization/Deployment/MY_App/image1.jpeg")  # image

st.image(img, caption="House")


st.write("<h1 style='font-family:Courier; background-color:yellow; color:black; font-size: 38px;'>Predict House Rent Prices</h1>",
         unsafe_allow_html=True)  # project title
st.markdown("""---""")


df = pd.read_csv(
    "/Users/anilfurkanembel/Desktop/Studies/Immo_Analyses_Visualization/Deployment/MY_App/Rent.csv")

choice1 = st.selectbox("Select the City:", ('region_Antwerp', 'region_Brussels', 'region_East Flanders',
                                            'region_Flemish Brabant', 'region_Hainaut', 'region_Limburg', 'region_Liège', 'region_Luxembourg', 'region_Namur', 'region_Walloon Brabant'))
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice1}  </h1>', unsafe_allow_html=True)
st.write("\n")

choice2 = st.selectbox("Select the House Type:", ('type_Appartement', 'type_Bungalow', 'type_Duplex', 'type_Logementétudiant',
                       'type_Maison', 'type_Maisondecampagne', 'type_Rez-de-chaussée', 'type_Studio', 'type_Triplex', 'type_Villa'))
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice2}  </h1>', unsafe_allow_html=True)

choice3 = st.number_input("Enter the m2 of the house :", min_value=0)
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice3}  </h1>', unsafe_allow_html=True)

choice4 = st.number_input("Enter Number Of Rooms:", min_value=1, max_value=7)
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice4}  </h1>', unsafe_allow_html=True)

choice5 = st.selectbox("Select the House Type for Furnished :", (1, 0))
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice5}  </h1>', unsafe_allow_html=True)

choice6 = st.selectbox("Select House Type for Garden :", (1, 0))
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice6}  </h1>', unsafe_allow_html=True)

choice7 = st.selectbox("Select Kitchen Type equipped :", (1, 0))
st.write(
    f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">{"You have selected :"}{choice7}  </h1>', unsafe_allow_html=True)


alpha_space = np.linspace(0.01, 100, 100)
X = df.drop(columns=["price"])
y = df.price
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=101)

# loading the linear regression model
lin_reg_model_R = LinearRegression()

# Fitting it into our model
lin_reg_model_R.fit(X_train, y_train)

# prediction on tarining data
training_data_prediction_R = lin_reg_model_R.predict(X_train)
pickle.dump(lin_reg_model_R, open('lin_reg_model_R', 'wb'))

anil_model = pickle.load(open('lin_reg_model_R', 'rb'))

my_dict = {
    choice1: 1,
    choice2: 1,
    "number_of_rooms": choice4,
    "living_area": choice3,
    "furnished": choice5,
    "garden": choice6,
    "fully_equipped_kitchen": choice7

}

test_df = pd.DataFrame.from_dict([my_dict])
test_df = test_df.reindex(columns=X.columns, fill_value=0)


prediction = anil_model.predict(test_df)
price = round(prediction[0], 3)


if st.button("Predict") and price > 0:
    pr = anil_model.predict(test_df)
    price = round(pr[0], 3)
    st.balloons()
    st.write(
        f'<h1 style="font-family:Courier; background-color:yellow;opacity: 0.9;text-align: center; color:black;;font-size:16px;">The price of the House : Eur{price}, </h1>', unsafe_allow_html=True)

if price < 0:
    st.write(f'<h1 style="font-family:Courier; background-color:black;opacity: 0.9;text-align: center; color:red;;font-size:16px;">!!! Wrong choice made !!! </h1>', unsafe_allow_html=True)
