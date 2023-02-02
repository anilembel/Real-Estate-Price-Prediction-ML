import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from model.UserRequest import UserRequest


class ModelManager:

    def __init__(self):
        df = pd.read_csv("model/Rent.csv")
        alpha_space = np.linspace(0.01, 100, 100)
        self.X = df.drop(columns=["price"])
        y = df.price
        X_train, X_test, y_train, y_test = train_test_split(self.X, y, test_size=0.2, random_state=101)

        lin_reg_model_R = LinearRegression()

        # Fitting it into our model
        lin_reg_model_R.fit(X_train, y_train)

        # prediction on tarining data
        training_data_prediction_R = lin_reg_model_R.predict(X_train)
        pickle.dump(lin_reg_model_R, open('lin_reg_model_R', 'wb'))

        self.anil_model = pickle.load(open('lin_reg_model_R', 'rb'))

    async def make_prediction(self, userRequest: UserRequest):
        userDict = userRequest.toModelDict()
        test_df = pd.DataFrame.from_dict([userDict])
        test_df = test_df.reindex(columns=self.X.columns, fill_value=0)
        prediction = self.anil_model.predict(test_df)
        price = round(prediction[0], 3)
        return price
